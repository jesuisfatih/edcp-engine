#!/usr/bin/env python3
"""Fix sync_manager.py indent issue"""

with open('sync_manager.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # Fix the problematic section (lines 612-625)
    if i == 611 and '# Save to database for rollback' in line:
        # This should be inside the try block, so fix indent
        new_lines.append('                        # Save to database for rollback\n')
        i += 1
        if i < len(lines) and '# Handle both dict' in lines[i]:
            new_lines.append('                        # Handle both dict and list formats for variants\n')
            i += 1
        if i < len(lines) and 'variants = result.get' in lines[i]:
            new_lines.append('                        variants = result.get(\'variants\', [])\n')
            i += 1
        if i < len(lines) and 'if isinstance(variants, list):' in lines[i]:
            new_lines.append('                        if isinstance(variants, list):\n')
            i += 1
        if i < len(lines) and 'for variant in variants:' in lines[i]:
            new_lines.append('                            for variant in variants:\n')
            i += 1
        if i < len(lines) and 'variant_id = variant.get' in lines[i]:
            new_lines.append('                                variant_id = variant.get(\'id\') if isinstance(variant, dict) else getattr(variant, \'id\', None)\n')
            i += 1
        if i < len(lines) and 'variant_sku = variant.get' in lines[i]:
            new_lines.append('                                variant_sku = variant.get(\'sku\', \'\') if isinstance(variant, dict) else getattr(variant, \'sku\', \'\')\n')
            i += 1
        if i < len(lines) and 'if variant_id and variant_sku:' in lines[i]:
            new_lines.append('                                if variant_id and variant_sku:\n')
            i += 1
        if i < len(lines) and 'save_sync_product' in lines[i]:
            new_lines.append('                                    save_sync_product(self.sync_id, result[\'id\'], variant_id, variant_sku, \'created\')\n')
            i += 1
        if i < len(lines) and '# Add to collections' in lines[i]:
            new_lines.append('                    \n')
            new_lines.append('                    # Add to collections if needed\n')
            i += 1
        if i < len(lines) and 'if self.sync_options.get(\'sync_collections\'' in lines[i]:
            new_lines.append('                    if self.sync_options.get(\'sync_collections\', True) and product_data.get(\'collections\'):\n')
            i += 1
        if i < len(lines) and 'for coll_id in product_data' in lines[i]:
            new_lines.append('                        for coll_id in product_data[\'collections\']:\n')
            i += 1
        if i < len(lines) and 'self.shopify_client.add_product_to_collection' in lines[i]:
            new_lines.append('                            self.shopify_client.add_product_to_collection(result[\'id\'], coll_id)\n')
            i += 1
        continue
    else:
        new_lines.append(line)
        i += 1

with open('sync_manager.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Fixed')

