# Warehouse Filter Implementation - TODO

## Completed (Backend):
✅ S&S API: `get_warehouses()` method
✅ Backend: `/api/warehouses` endpoint
✅ DataFetcher: Warehouse filter parameter

## Remaining (Frontend):
⏳ UI: Warehouse selection (filtreleme ekranının EN BAŞINDA)
⏳ UI: Show stock per warehouse
⏳ UI: "En çok stoklu lokasyon" checkbox
⏳ Save selected warehouses to sync_options
⏳ Test with warehouse filter

## Expected Result:
When warehouse filter applied:
- 252 SKUs (multi-location) → 80 variants (single location)
- No duplicate "White / S" variants
- Clean, correct Shopify sync

## Next Session:
1. Add warehouse selection UI (top of filter screen)
2. Load warehouses via /api/warehouses
3. Show checkboxes with stock counts
4. Test with single warehouse
5. Verify no duplicates

