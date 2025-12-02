"""
Domain Models - Style-centric domain layer (Shopify-agnostic)

These models represent the business domain (catalog/product reality)
independent of Shopify's data structure.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
import hashlib
import json


@dataclass
class StyleVariant:
    """Represents a single SKU/variant of a style - may aggregate multiple warehouse SKUs"""
    sku: str  # Primary SKU (first or highest stock)
    skus: List[str] = field(default_factory=list)  # All SKUs for this variant (if merged)
    color_name: str = ""
    color_code: str = ""
    size_name: str = ""
    size_code: str = ""
    price: float = 0.0
    barcode: Optional[str] = None
    weight: float = 0.0
    weight_unit: str = 'lb'
    
    # Multi-location inventory support
    inventory_quantity: Optional[int] = None  # Total inventory (sum of all locations)
    location_inventory: Dict[str, int] = field(default_factory=dict)  # {warehouse_code: qty}
    
    image_url: Optional[str] = None
    
    # Raw metafields
    metafields: Dict = field(default_factory=dict)
    
    def __post_init__(self):
        """Ensure color and size have values (fallback to SKU if empty)"""
        # CRITICAL: Aggressive normalization to prevent Shopify duplicates
        if self.color_name:
            self.color_name = ' '.join(self.color_name.strip().split())  # Normalize whitespace
        else:
            self.color_name = f"Color-{self.sku[:10]}" if self.sku else "Default"
        
        if self.size_name:
            self.size_name = ' '.join(self.size_name.strip().split())  # Normalize whitespace
        else:
            self.size_name = f"Size-{self.sku[:10]}" if self.sku else "OneSize"
    
    @property
    def option_key(self) -> tuple:
        """Unique key for this variant's options (for deduplication)"""
        # CRITICAL: Case-insensitive and whitespace-safe comparison
        return (
            self.color_name.strip().lower() if self.color_name else '',
            self.size_name.strip().lower() if self.size_name else ''
        )
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'sku': self.sku,
            'color_name': self.color_name,
            'size_name': self.size_name,
            'price': str(self.price),
            'barcode': self.barcode,
            'weight': self.weight,
            'weight_unit': self.weight_unit,
            'inventory_quantity': self.inventory_quantity,
            'image_url': self.image_url,
            'metafields': self.metafields
        }


@dataclass
class StyleImage:
    """Represents a product-level image"""
    url: str
    alt_text: Optional[str] = None
    position: int = 0


@dataclass
class Style:
    """
    Domain model representing a complete Style (one logical product)
    Independent of Shopify's structure
    """
    style_id: str
    brand: str
    name: str
    description: str = ""
    product_type: str = ""
    
    # Variants (all color/size combinations)
    variants: List[StyleVariant] = field(default_factory=list)
    
    # Images (product-level)
    images: List[StyleImage] = field(default_factory=list)
    
    # Tags and categorization
    tags: List[str] = field(default_factory=list)
    
    # Product-level metafields
    metafields: Dict = field(default_factory=dict)
    
    # Collections this style belongs to
    collections: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Validation and normalization"""
        if not self.style_id:
            raise ValueError("style_id is required")
        if not self.variants:
            raise ValueError("Style must have at least one variant")
    
    @property
    def variant_count(self) -> int:
        """Total number of variants"""
        return len(self.variants)
    
    # Shopify GraphQL API supports up to 2048 variants per product (as of 2024-04)
    # Previously was 100 with REST API
    MAX_VARIANTS_PER_PRODUCT = 2048
    
    @property
    def requires_split(self) -> bool:
        """Does this style exceed Shopify's 2048-variant limit?"""
        return self.variant_count > self.MAX_VARIANTS_PER_PRODUCT
    
    @property
    def split_count(self) -> int:
        """How many Shopify products needed for this style?"""
        if not self.requires_split:
            return 1
        # Calculate number of products needed (2048 variants each)
        return (self.variant_count + self.MAX_VARIANTS_PER_PRODUCT - 1) // self.MAX_VARIANTS_PER_PRODUCT
    
    def compute_snapshot_hash(self) -> str:
        """
        Compute deterministic hash of this style's current state
        Used for change detection (skip unchanged styles)
        """
        # Build deterministic representation
        snapshot = {
            'style_id': self.style_id,
            'variant_count': self.variant_count,
            'variants': sorted([
                {
                    'sku': v.sku,
                    'price': str(v.price),
                    'color': v.color_name,
                    'size': v.size_name,
                    'inventory': v.inventory_quantity
                }
                for v in self.variants
            ], key=lambda x: x['sku'])
        }
        
        # SHA256 hash
        snapshot_json = json.dumps(snapshot, sort_keys=True)
        return hashlib.sha256(snapshot_json.encode()).hexdigest()
    
    def split_into_parts(self, max_variants_per_part: int = 2048) -> List['StylePart']:
        """
        Split this style into multiple parts if variant count > max
        Returns list of StylePart objects
        """
        if not self.requires_split:
            # Single part
            return [StylePart(
                style=self,
                part_index=0,
                variants=self.variants,
                total_parts=1
            )]
        
        # Split variants into parts
        parts = []
        total_parts = self.split_count
        
        for part_index in range(total_parts):
            start_idx = part_index * max_variants_per_part
            end_idx = min(start_idx + max_variants_per_part, self.variant_count)
            part_variants = self.variants[start_idx:end_idx]
            
            parts.append(StylePart(
                style=self,
                part_index=part_index,
                variants=part_variants,
                total_parts=total_parts
            ))
        
        return parts
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'style_id': self.style_id,
            'brand': self.brand,
            'name': self.name,
            'description': self.description,
            'product_type': self.product_type,
            'variant_count': self.variant_count,
            'variants': [v.to_dict() for v in self.variants],
            'images': [{'url': img.url, 'alt': img.alt_text} for img in self.images],
            'tags': self.tags,
            'metafields': self.metafields
        }


@dataclass
class StylePart:
    """
    Represents one part of a split style
    Used when a style has >100 variants and must be split into multiple Shopify products
    """
    style: Style
    part_index: int
    variants: List[StyleVariant]
    total_parts: int
    
    @property
    def title(self) -> str:
        """Generate title for this part"""
        base_title = f"{self.style.brand} {self.style.name}"
        
        if self.total_parts > 1:
            # Multi-part product
            return f"{base_title} (Part {self.part_index + 1}/{self.total_parts})"
        
        return base_title
    
    @property
    def variant_count(self) -> int:
        return len(self.variants)
    
    def to_dict(self) -> Dict:
        """Convert to dictionary"""
        return {
            'style_id': self.style.style_id,
            'part_index': self.part_index,
            'total_parts': self.total_parts,
            'title': self.title,
            'variant_count': self.variant_count,
            'variants': [v.to_dict() for v in self.variants]
        }


@dataclass
class ShopifyProduct:
    """Represents actual state of a Shopify product"""
    product_id: int
    product_gid: str
    title: str
    handle: str
    variant_count: int
    variants: List[Dict] = field(default_factory=list)  # List of {id, sku, ...}
    
    def to_dict(self) -> Dict:
        return {
            'id': self.product_id,
            'gid': self.product_gid,
            'title': self.title,
            'handle': self.handle,
            'variant_count': self.variant_count,
            'variants': self.variants
        }


@dataclass
class DesiredShopifyState:
    """What should exist in Shopify for a given style"""
    style_id: str
    parts: List[StylePart]  # 1 or more Shopify products
    
    @property
    def total_variants(self) -> int:
        return sum(part.variant_count for part in self.parts)
    
    def to_dict(self) -> Dict:
        return {
            'style_id': self.style_id,
            'total_parts': len(self.parts),
            'total_variants': self.total_variants,
            'parts': [part.to_dict() for part in self.parts]
        }


@dataclass
class ActualShopifyState:
    """What currently exists in Shopify for a given style"""
    style_id: str
    products: List[ShopifyProduct] = field(default_factory=list)
    
    @property
    def product_count(self) -> int:
        return len(self.products)
    
    @property
    def total_variants(self) -> int:
        return sum(p.variant_count for p in self.products)
    
    def to_dict(self) -> Dict:
        return {
            'style_id': self.style_id,
            'product_count': self.product_count,
            'total_variants': self.total_variants,
            'products': [p.to_dict() for p in self.products]
        }

