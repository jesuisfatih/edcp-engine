"""
Reconciliation Layer - Compares desired vs actual Shopify state

Generates delta operations to sync Shopify with desired state
"""

from domain_models import Style, StylePart, DesiredShopifyState, ActualShopifyState, ShopifyProduct
from database import get_db
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class OperationType(Enum):
    """Types of sync operations"""
    CREATE_PRODUCT = "create_product"
    UPDATE_PRODUCT = "update_product"
    CREATE_VARIANT = "create_variant"
    UPDATE_VARIANT = "update_variant"
    DELETE_VARIANT = "delete_variant"
    UPDATE_INVENTORY = "update_inventory"
    ADD_IMAGES = "add_images"
    UPDATE_METAFIELDS = "update_metafields"
    ADD_TO_COLLECTIONS = "add_to_collections"


@dataclass
class SyncOperation:
    """Represents a single sync operation"""
    operation_type: OperationType
    style_id: str
    part_index: int = 0
    payload: Dict = None
    
    def to_dict(self) -> Dict:
        return {
            'type': self.operation_type.value,
            'style_id': self.style_id,
            'part_index': self.part_index,
            'payload': self.payload
        }


class StyleMapper:
    """Maps Style IDs to Shopify Product IDs (persistent)"""
    
    @staticmethod
    def get_shopify_products_for_style(style_id: str) -> List[Tuple[int, int, str]]:
        """
        Get all Shopify products for a style
        Returns: List of (part_index, shopify_product_id, shopify_gid)
        """
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT part_index, shopify_product_id, shopify_gid
                FROM style_shopify_products
                WHERE style_id = ?
                ORDER BY part_index
            ''', (style_id,))
            
            return [(row['part_index'], row['shopify_product_id'], row['shopify_gid']) 
                    for row in cursor.fetchall()]
    
    @staticmethod
    def save_style_product_mapping(style_id: str, part_index: int, 
                                    shopify_product_id: int, shopify_gid: str,
                                    shopify_handle: str, variant_count: int,
                                    snapshot_hash: str):
        """Save or update style → Shopify product mapping"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO style_shopify_products 
                (style_id, part_index, shopify_product_id, shopify_gid, shopify_handle, 
                 variant_count, snapshot_hash, updated_at, last_synced_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                ON CONFLICT(style_id, part_index) DO UPDATE SET
                    shopify_product_id = excluded.shopify_product_id,
                    shopify_gid = excluded.shopify_gid,
                    shopify_handle = excluded.shopify_handle,
                    variant_count = excluded.variant_count,
                    snapshot_hash = excluded.snapshot_hash,
                    updated_at = CURRENT_TIMESTAMP,
                    last_synced_at = CURRENT_TIMESTAMP
            ''', (style_id, part_index, shopify_product_id, shopify_gid, 
                  shopify_handle, variant_count, snapshot_hash))
    
    @staticmethod
    def save_sku_variant_mapping(sku: str, style_id: str, 
                                  shopify_variant_id: int, shopify_product_id: int,
                                  shopify_gid: str):
        """Save SKU → Shopify variant mapping"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO sku_shopify_variants
                (sku, style_id, shopify_variant_id, shopify_product_id, shopify_gid, updated_at)
                VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(sku) DO UPDATE SET
                    shopify_variant_id = excluded.shopify_variant_id,
                    shopify_product_id = excluded.shopify_product_id,
                    shopify_gid = excluded.shopify_gid,
                    updated_at = CURRENT_TIMESTAMP
            ''', (sku, style_id, shopify_variant_id, shopify_product_id, shopify_gid))
    
    @staticmethod
    def get_last_snapshot_hash(style_id: str) -> Optional[str]:
        """Get last snapshot hash for change detection"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT snapshot_hash FROM style_snapshots
                WHERE style_id = ?
                ORDER BY created_at DESC
                LIMIT 1
            ''', (style_id,))
            
            row = cursor.fetchone()
            return row['snapshot_hash'] if row else None
    
    @staticmethod
    def save_snapshot(style_id: str, snapshot_hash: str, variant_count: int, 
                     snapshot_data: str):
        """Save new snapshot"""
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO style_snapshots
                (style_id, snapshot_hash, variant_count, snapshot_data)
                VALUES (?, ?, ?, ?)
            ''', (style_id, snapshot_hash, variant_count, snapshot_data))


class Reconciler:
    """
    Reconciles desired Shopify state with actual state
    Generates list of operations to apply
    """
    
    def __init__(self, shopify_client):
        self.shopify_client = shopify_client
    
    def build_desired_state(self, style: Style) -> DesiredShopifyState:
        """
        Convert Style domain object into desired Shopify state
        Handles 2048-variant split if needed (rarely necessary now)
        """
        parts = style.split_into_parts(max_variants_per_part=2048)
        
        return DesiredShopifyState(
            style_id=style.style_id,
            parts=parts
        )
    
    def fetch_actual_state(self, style_id: str) -> ActualShopifyState:
        """
        Fetch current Shopify state for this style
        Uses persistent mapping to find products
        """
        # Get mapped Shopify products
        mappings = StyleMapper.get_shopify_products_for_style(style_id)
        
        products = []
        for part_index, shopify_product_id, shopify_gid in mappings:
            # Fetch product from Shopify
            try:
                product_data = self.shopify_client.get_product_by_id(shopify_product_id)
                if product_data:
                    products.append(ShopifyProduct(
                        product_id=shopify_product_id,
                        product_gid=shopify_gid,
                        title=product_data.get('title', ''),
                        handle=product_data.get('handle', ''),
                        variant_count=len(product_data.get('variants', [])),
                        variants=product_data.get('variants', [])
                    ))
            except:
                # Product not found or deleted
                pass
        
        return ActualShopifyState(
            style_id=style_id,
            products=products
        )
    
    def reconcile(self, desired: DesiredShopifyState, actual: ActualShopifyState) -> List[SyncOperation]:
        """
        Compare desired vs actual, generate operations
        """
        operations = []
        
        # For each desired part
        for part in desired.parts:
            part_idx = part.part_index
            
            # Check if this part exists in actual
            actual_product = None
            for p in actual.products:
                # Match by part index (from mapping)
                # In practice we'd track part_index in mapping
                if len(actual.products) > part_idx:
                    actual_product = actual.products[part_idx]
                    break
            
            if not actual_product:
                # CREATE new product
                operations.append(SyncOperation(
                    operation_type=OperationType.CREATE_PRODUCT,
                    style_id=desired.style_id,
                    part_index=part_idx,
                    payload={
                        'part': part.to_dict(),
                        'style': part.style.to_dict()
                    }
                ))
            else:
                # UPDATE existing product
                operations.append(SyncOperation(
                    operation_type=OperationType.UPDATE_PRODUCT,
                    style_id=desired.style_id,
                    part_index=part_idx,
                    payload={
                        'shopify_product_id': actual_product.product_id,
                        'part': part.to_dict(),
                        'style': part.style.to_dict()
                    }
                ))
        
        return operations
    
    def should_sync_style(self, style: Style) -> bool:
        """
        Check if style needs syncing (change detection)
        Returns True if style changed since last sync
        """
        current_hash = style.compute_snapshot_hash()
        last_hash = StyleMapper.get_last_snapshot_hash(style.style_id)
        
        if last_hash == current_hash:
            print(f"  Style {style.style_id} unchanged (hash match), skipping...")
            return False
        
        print(f"  Style {style.style_id} changed (hash mismatch), will sync")
        return True


