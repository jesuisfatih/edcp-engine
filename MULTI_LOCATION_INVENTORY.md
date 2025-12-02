# Multi-Location Inventory Implementation

## Problem
S&S Activewear API returns multiple SKUs for same color/size combination:
- B00185020: Electric Blue / M → Warehouse CA: 95
- B00185021: Electric Blue / M → Warehouse TX: 275

Previously, each SKU became a separate Shopify variant:
- Electric Blue 20 / M (stock: 95)
- Electric Blue 21 / M (stock: 275)

This is incorrect and confusing.

## Solution: Multi-Location Inventory

### Step 1: Merge Same Color/Size
In StyleBuilder, merge variants with same (color, size):
- Keep first SKU as primary
- Aggregate all SKUs
- Sum inventory by location

### Step 2: Store Location-Level Inventory
```python
StyleVariant(
    sku="B00185020",  # Primary SKU
    skus=["B00185020", "B00185021"],  # All SKUs
    color_name="Electric Blue",
    size_name="M",
    inventory_quantity=370,  # Total
    location_inventory={
        "CA": 95,
        "TX": 275
    }
)
```

### Step 3: Create Shopify Locations
Map S&S warehouses to Shopify locations:
- CA → Location ID: xxx
- TX → Location ID: yyy

### Step 4: Sync with Multi-Location Inventory
Use Shopify's `inventoryQuantities` field:
```json
{
  "variant": {
    "option1": "Electric Blue",
    "option2": "M",
    "sku": "B00185020",
    "price": "10.00",
    "inventoryQuantities": [
      {"locationId": "gid://shopify/Location/xxx", "availableQuantity": 95},
      {"locationId": "gid://shopify/Location/yyy", "availableQuantity": 275}
    ]
  }
}
```

## Benefits
✅ Correct product structure (1 variant per color/size)
✅ Accurate inventory tracking (location-aware)
✅ No duplicate variants
✅ Professional e-commerce setup

