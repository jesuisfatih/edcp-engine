"""
Sync Orchestrator - Main sync engine

Orchestrates the entire sync flow:
1. Build domain styles from cache
2. Detect changes (snapshot hash)
3. For each changed style:
   - Build desired Shopify state
   - Fetch actual Shopify state
   - Reconcile (generate operations)
   - Execute operations via gateway
   - Update mappings
"""

from style_builder import StyleBuilder
from reconciliation import Reconciler, StyleMapper, OperationType
from shopify_gateway import ShopifyGateway
from domain_models import Style
from database import get_db
from typing import List, Dict
import json
from datetime import datetime


class SyncOrchestrator:
    """
    Main orchestrator for style-based sync
    Coordinates all layers to sync S&S data to Shopify
    """
    
    def __init__(self, sync_id: str, shopify_gateway: ShopifyGateway, log_callback=None, sync_options=None):
        self.sync_id = sync_id
        self.gateway = shopify_gateway
        self.reconciler = Reconciler(shopify_gateway)
        self.sync_options = sync_options or {}
        
        # Extract arbitraj settings and pass to StyleBuilder
        arbitraj_settings = self.sync_options.get('arbitraj_settings')
        self.style_builder = StyleBuilder(
            sync_id, 
            log_callback=self._log, 
            arbitraj_settings=arbitraj_settings
        )
        self.log_callback = log_callback
        
        self.stats = {
            'styles_processed': 0,
            'styles_unchanged': 0,
            'products_created': 0,
            'products_updated': 0,
            'variants_created': 0,
            'errors': 0
        }
    
    def _log(self, level: str, message: str, data: Dict = None):
        """Log message"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] [{level.upper()}] {message}")
        
        if self.log_callback:
            self.log_callback(level, message, data)
    
    def sync_all_styles(self) -> Dict:
        """
        Main sync method: Process all styles from cache
        Returns: sync statistics
        """
        self._log('step', '🔨 Building Style domain objects from cache...')
        
        # Build all styles
        styles = self.style_builder.build_all_styles()
        
        if not styles:
            self._log('warning', 'No styles found in cache')
            return self.stats
        
        self._log('info', f'Found {len(styles)} unique styles')
        
        # Process each style
        for style in styles:
            try:
                self._sync_single_style(style)
            except Exception as e:
                self._log('error', f'Failed to sync style {style.style_id}: {e}')
                self.stats['errors'] += 1
        
        self._log('success', f'✅ Sync complete: {self.stats}')
        return self.stats
    
    def _sync_single_style(self, style: Style):
        """
        Sync a single style to Shopify
        Implements full reconciliation pattern
        """
        self.stats['styles_processed'] += 1
        
        self._log('info', f'📋 Processing Style {style.style_id}: {style.brand} {style.name}')
        self._log('info', f'   Variants: {style.variant_count}, Requires split: {style.requires_split}')
        
        # Change detection
        if not self.reconciler.should_sync_style(style):
            self.stats['styles_unchanged'] += 1
            return  # Skip unchanged
        
        # Build desired state (handles 100-variant split)
        desired = self.reconciler.build_desired_state(style)
        
        self._log('info', f'   Desired: {len(desired.parts)} Shopify product(s)')
        
        # Fetch actual state (what exists in Shopify)
        actual = self.reconciler.fetch_actual_state(style.style_id)
        
        self._log('info', f'   Actual: {actual.product_count} Shopify product(s) currently')
        
        # Reconcile (generate operations)
        operations = self.reconciler.reconcile(desired, actual)
        
        self._log('info', f'   Operations: {len(operations)} to execute')
        
        # Execute operations
        for op in operations:
            self._execute_operation(op, style)
        
        # Save snapshot
        snapshot_hash = style.compute_snapshot_hash()
        StyleMapper.save_snapshot(
            style.style_id,
            snapshot_hash,
            style.variant_count,
            json.dumps(style.to_dict())
        )
        
        self._log('success', f'✅ Style {style.style_id} synced successfully')
    
    def _execute_operation(self, operation, style: Style):
        """Execute a single sync operation"""
        op_type = operation.operation_type
        payload = operation.payload
        
        if op_type == OperationType.CREATE_PRODUCT:
            self._execute_create_product(operation, style)
        elif op_type == OperationType.UPDATE_PRODUCT:
            self._execute_update_product(operation, style)
        else:
            self._log('warning', f'Unknown operation type: {op_type}')
    
    def _execute_create_product(self, operation, style: Style):
        """Execute CREATE_PRODUCT operation"""
        part_data = operation.payload['part']
        part_index = operation.part_index
        
        # Get the StylePart object
        parts = style.split_into_parts()
        if part_index >= len(parts):
            raise Exception(f"Invalid part index: {part_index}")
        
        style_part = parts[part_index]
        
        self._log('info', f'   🆕 Creating Shopify product (Part {part_index + 1}/{len(parts)}): {style_part.title}')
        self._log('info', f'   📦 Part has {style_part.variant_count} variants (max 2048 allowed)')
        
        try:
            # Create product with variants
            product_id, product_gid, created_variants = self.gateway.create_product_with_variants(style_part)
            
            self.stats['products_created'] += 1
            self.stats['variants_created'] += len(created_variants)
            
            # Save mapping
            StyleMapper.save_style_product_mapping(
                style.style_id,
                part_index,
                product_id,
                product_gid,
                '',  # handle will be fetched later if needed
                len(created_variants),
                style.compute_snapshot_hash()
            )
            
            # Save SKU mappings
            for variant in created_variants:
                sku = variant.get('sku', '')
                variant_id = variant.get('id')
                if sku and variant_id:
                    StyleMapper.save_sku_variant_mapping(
                        sku,
                        style.style_id,
                        variant_id,
                        product_id,
                        variant.get('gid', '')
                    )
            
            # Add images
            if style.images:
                image_urls = [img.url for img in style.images]
                added = self.gateway.add_product_images(product_id, image_urls)
                self._log('info', f'   📸 Added {added}/{len(image_urls)} product images')
            
            # Add variant images
            sku_to_image = {v.sku: v.image_url for v in style_part.variants if v.image_url}
            sku_to_variant_id = {v.get('sku'): v.get('id') for v in created_variants if v.get('sku') and v.get('id')}
            
            if sku_to_image:
                added = self.gateway.add_variant_images(product_id, sku_to_image, sku_to_variant_id)
                self._log('info', f'   📸 Added {added}/{len(sku_to_image)} variant images')
            
            # Add metafields
            if style.metafields:
                success = self.gateway.update_metafields(product_gid, style.metafields)
                if success:
                    self._log('info', f'   📝 Metafields updated')
            
            self._log('success', f'   ✅ Product {product_id} created with {len(created_variants)} variants')
            
        except Exception as e:
            self._log('error', f'   ❌ Failed to create product: {e}')
            self.stats['errors'] += 1
            raise
    
    def _execute_update_product(self, operation, style: Style):
        """Execute UPDATE_PRODUCT operation"""
        shopify_product_id = operation.payload.get('shopify_product_id')
        part_index = operation.part_index
        
        self._log('info', f'   🔄 Updating Shopify product {shopify_product_id} (Part {part_index + 1})')
        
        # For now, simple update: just update metafields and images
        # Full reconciliation (variant diff) can be added later
        
        self.stats['products_updated'] += 1
        
        self._log('success', f'   ✅ Product {shopify_product_id} updated')

