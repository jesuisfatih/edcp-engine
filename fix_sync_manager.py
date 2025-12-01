#!/usr/bin/env python3
"""Fix sync_manager.py - add try-except block for create_product"""

import sys

# Read the file
with open('sync_manager.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line with "if self.sync_options.get('create_new', True):"
# and replace the following block
new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    
    # Check if this is the line we need to modify
    if 'if self.sync_options.get(\'create_new\', True):' in line and i > 580:
        # Add the try block
        new_lines.append(line)
        new_lines.append('                try:\n')
        i += 1
        
        # Skip the old code and replace it
        if 'result = self.shopify_client.create_product(product_data)' in lines[i]:
            # Add new code
            new_lines.append('                    result = self.shopify_client.create_product(product_data)\n')
            new_lines.append('                    \n')
            new_lines.append('                    # Check if product already exists (create_product might return existing product)\n')
            new_lines.append('                    if result.get(\'status\') == \'exists\':\n')
            new_lines.append('                        # Product already exists, update it instead\n')
            new_lines.append('                        print(f"Product already exists, updating instead: {result[\'id\']}")\n')
            new_lines.append('                        self.shopify_client.update_product(result[\'id\'], product_data)\n')
            new_lines.append('                        self.stats[\'updated\'] += 1\n')
            new_lines.append('                        # Save to database for rollback\n')
            new_lines.append('                        variants = result.get(\'variants\', [])\n')
            new_lines.append('                        if variants:\n')
            new_lines.append('                            for variant in variants:\n')
            new_lines.append('                                variant_id = variant.get(\'id\') if isinstance(variant, dict) else None\n')
            new_lines.append('                                variant_sku = variant.get(\'sku\', \'\') if isinstance(variant, dict) else \'\'\n')
            new_lines.append('                                if variant_id and variant_sku:\n')
            new_lines.append('                                    save_sync_product(self.sync_id, result[\'id\'], variant_id, variant_sku, \'updated\')\n')
            new_lines.append('                    else:\n')
            new_lines.append('                        # New product created\n')
            new_lines.append('                        self.stats[\'created\'] += 1\n')
            new_lines.append('                        # Save to database for rollback\n')
            new_lines.append('                        variants = result.get(\'variants\', [])\n')
            new_lines.append('                        if isinstance(variants, list):\n')
            new_lines.append('                            for variant in variants:\n')
            new_lines.append('                                variant_id = variant.get(\'id\') if isinstance(variant, dict) else getattr(variant, \'id\', None)\n')
            new_lines.append('                                variant_sku = variant.get(\'sku\', \'\') if isinstance(variant, dict) else getattr(variant, \'sku\', \'\')\n')
            new_lines.append('                                if variant_id and variant_sku:\n')
            new_lines.append('                                    save_sync_product(self.sync_id, result[\'id\'], variant_id, variant_sku, \'created\')\n')
            new_lines.append('                    \n')
            new_lines.append('                    # Add to collections if needed\n')
            new_lines.append('                    if self.sync_options.get(\'sync_collections\', True) and product_data.get(\'collections\'):\n')
            new_lines.append('                        for coll_id in product_data[\'collections\']:\n')
            new_lines.append('                            self.shopify_client.add_product_to_collection(result[\'id\'], coll_id)\n')
            new_lines.append('                except Exception as e:\n')
            new_lines.append('                    error_msg = str(e)\n')
            new_lines.append('                    # If error is about variant already existing, try to find product by title and update\n')
            new_lines.append('                    if \'variant\' in error_msg.lower() and \'already exists\' in error_msg.lower():\n')
            new_lines.append('                        # Try to find product by title from product_data\n')
            new_lines.append('                        product_title = product_data.get(\'title\', \'\')\n')
            new_lines.append('                        if product_title:\n')
            new_lines.append('                            try:\n')
            new_lines.append('                                import requests\n')
            new_lines.append('                                # Search for product by title\n')
            new_lines.append('                                search_response = requests.get(\n')
            new_lines.append('                                    f"{self.shopify_client.base_url}/products.json",\n')
            new_lines.append('                                    headers=self.shopify_client.headers,\n')
            new_lines.append('                                    params={\'title\': product_title, \'limit\': 10},\n')
            new_lines.append('                                    timeout=30\n')
            new_lines.append('                                )\n')
            new_lines.append('                                if search_response.status_code == 200:\n')
            new_lines.append('                                    search_products = search_response.json().get(\'products\', [])\n')
            new_lines.append('                                    for search_product in search_products:\n')
            new_lines.append('                                        if search_product.get(\'title\', \'\').strip().lower() == product_title.strip().lower():\n')
            new_lines.append('                                            # Found existing product, update it\n')
            new_lines.append('                                            print(f"Found existing product by title after error, updating: {search_product[\'id\']}")\n')
            new_lines.append('                                            self.shopify_client.update_product(search_product[\'id\'], product_data)\n')
            new_lines.append('                                            self.stats[\'updated\'] += 1\n')
            new_lines.append('                                            # Save to database\n')
            new_lines.append('                                            variants = search_product.get(\'variants\', [])\n')
            new_lines.append('                                            if variants:\n')
            new_lines.append('                                                for variant in variants:\n')
            new_lines.append('                                                    variant_id = variant.get(\'id\')\n')
            new_lines.append('                                                    variant_sku = variant.get(\'sku\', \'\')\n')
            new_lines.append('                                                    if variant_id and variant_sku:\n')
            new_lines.append('                                                        save_sync_product(self.sync_id, search_product[\'id\'], variant_id, variant_sku, \'updated\')\n')
            new_lines.append('                                            return  # Success, exit\n')
            new_lines.append('                            except Exception as search_error:\n')
            new_lines.append('                                print(f"Error searching for product by title: {search_error}")\n')
            new_lines.append('                    \n')
            new_lines.append('                    # If we get here, the error couldn\'t be resolved\n')
            new_lines.append('                    raise\n')
            
            # Skip old lines until we find the else or next function
            while i < len(lines):
                i += 1
                if i >= len(lines):
                    break
                if 'else:' in lines[i] and 'self.stats[\'skipped\']' in lines[i+1] if i+1 < len(lines) else False:
                    new_lines.append(lines[i])
                    new_lines.append(lines[i+1])
                    i += 2
                    break
                if 'def _sync_product' in lines[i]:
                    new_lines.append(lines[i])
                    break
        else:
            new_lines.append(lines[i])
            i += 1
    else:
        new_lines.append(line)
        i += 1

# Write back
with open('sync_manager.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('File updated successfully')

