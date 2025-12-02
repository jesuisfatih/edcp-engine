// Warehouse selection UI functions

let selectedWarehouses = [];
let warehousesData = [];
let previewProducts = []; // Store preview products for stock detail modal

// Immediately export to window
if (typeof window !== 'undefined') {
    window.selectedWarehouses = selectedWarehouses;
}

async function loadWarehouses() {
    try {
        const ssAccountNumber = document.getElementById('ssAccountNumber').value;
        const ssApiKey = document.getElementById('ssApiKey').value;
        
        if (!ssAccountNumber || !ssApiKey) {
            alert('Önce S&S Activewear bilgilerini girin');
            return;
        }
        
        const response = await fetch('/api/warehouses', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                ss_account_number: ssAccountNumber,
                ss_api_key: ssApiKey
            })
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            warehousesData = data.warehouses || [];
            displayWarehouses(warehousesData);
            
            // Auto-select highest stock if checkbox checked
            if (document.getElementById('autoSelectHighestStock').checked && warehousesData.length > 0) {
                selectedWarehouses = [warehousesData[0].code];
                document.getElementById(`warehouse-${warehousesData[0].code}`).checked = true;
            }
        } else {
            alert('Lokasyonlar yüklenemedi: ' + data.message);
        }
    } catch (error) {
        alert('Hata: ' + error.message);
    }
}

function displayWarehouses(warehouses) {
    const container = document.getElementById('warehousesList');
    
    if (!warehouses || warehouses.length === 0) {
        container.innerHTML = '<p class="text-muted text-center">Lokasyon bulunamadı</p>';
        return;
    }
    
    let html = '<div class="list-group">';
    
    warehouses.forEach((wh, index) => {
        const stockBadge = wh.total_stock > 0 
            ? `<span class="badge bg-success">${wh.total_stock.toLocaleString()} adet</span>`
            : `<span class="badge bg-secondary">Stok yok</span>`;
        
        html += `
            <div class="list-group-item">
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" 
                           id="warehouse-${wh.code}" 
                           value="${wh.code}"
                           onchange="toggleWarehouse('${wh.code}')">
                    <label class="form-check-label d-flex justify-content-between align-items-center" 
                           for="warehouse-${wh.code}">
                        <span>
                            <strong>${wh.name || wh.code}</strong>
                            <small class="text-muted">(${wh.code})</small>
                        </span>
                        ${stockBadge}
                    </label>
                </div>
            </div>
        `;
    });
    
    html += '</div>';
    container.innerHTML = html;
}

function toggleWarehouse(code) {
    const checkbox = document.getElementById(`warehouse-${code}`);
    
    if (checkbox.checked) {
        if (!selectedWarehouses.includes(code)) {
            selectedWarehouses.push(code);
        }
    } else {
        selectedWarehouses = selectedWarehouses.filter(w => w !== code);
    }
    
    console.log('Selected warehouses:', selectedWarehouses);
    
    // Enable Step 1 (Kategoriler) if at least one warehouse selected
    if (selectedWarehouses.length > 0) {
        document.getElementById('step1-tab').disabled = false;
        document.getElementById('step1-tab').classList.remove('disabled');
        
        // Show continue button
        showWarehouseContinueButton();
    } else {
        document.getElementById('step1-tab').disabled = true;
        document.getElementById('step1-tab').classList.add('disabled');
    }
}

function showWarehouseContinueButton() {
    const container = document.getElementById('warehousesList');
    const existingBtn = document.getElementById('warehouseContinueBtn');
    
    if (!existingBtn) {
        const btn = document.createElement('button');
        btn.id = 'warehouseContinueBtn';
        btn.className = 'btn btn-success mt-3 w-100';
        btn.innerHTML = '<i class="fas fa-arrow-right"></i> Devam Et (Kategoriler)';
        btn.onclick = () => {
            document.getElementById('step1-tab').click();
        };
        container.parentElement.appendChild(btn);
    }
}

function getSelectedWarehouses() {
    return selectedWarehouses;
}

async function loadPreviewWithLocations() {
    try {
        const ssAccountNumber = document.getElementById('ssAccountNumber').value;
        const ssApiKey = document.getElementById('ssApiKey').value;
        
        if (!ssAccountNumber || !ssApiKey) {
            alert('S&S bilgileri eksik');
            return;
        }
        
        const container = document.getElementById('previewWithLocations');
        container.innerHTML = '<p class="text-info text-center"><i class="fas fa-spinner fa-spin"></i> Yükleniyor...</p>';
        
        const syncOptions = window.getSyncOptions ? window.getSyncOptions() : {};
        
        // Call BOTH preview and warehouses APIs in parallel
        const [previewResponse, warehouseResponse] = await Promise.all([
            fetch('/api/preview', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    ss_account_number: ssAccountNumber,
                    ss_api_key: ssApiKey,
                    sync_options: syncOptions
                })
            }),
            fetch('/api/warehouses', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    ss_account_number: ssAccountNumber,
                    ss_api_key: ssApiKey
                })
            })
        ]);
        
        const previewData = await previewResponse.json();
        const warehouseData = await warehouseResponse.json();
        
        console.log('Preview response:', previewData);
        console.log('Warehouse response:', warehouseData);
        
        // Check for errors
        if (previewData.status === 'error') {
            container.innerHTML = `<div class="alert alert-danger"><strong>Hata:</strong> ${previewData.message || 'Preview yüklenemedi'}</div>`;
            return;
        }
        
        if (warehouseData.status === 'error') {
            container.innerHTML = `<div class="alert alert-danger"><strong>Hata:</strong> ${warehouseData.message || 'Lokasyonlar yüklenemedi'}</div>`;
            return;
        }
        
        const productCount = previewData.count || 0;
        const warehouses = warehouseData.warehouses || [];
        
        // Store products for stock detail modal
        previewProducts = previewData.products || [];
        console.log('Preview products stored:', previewProducts.length);
        
        displayPreviewWithLocations(productCount, warehouses, previewProducts);
        
    } catch (error) {
        alert('Hata: ' + error.message);
        console.error('Preview error:', error);
    }
}

function displayPreviewWithLocations(productCount, warehouses, products = []) {
    const container = document.getElementById('previewWithLocations');
    
    if (productCount === 0) {
        container.innerHTML = '<p class="text-warning">Seçilen filtrelere uygun ürün bulunamadı</p>';
        return;
    }
    
    if (!warehouses || warehouses.length === 0) {
        container.innerHTML = `
            <div class="alert alert-success">
                <strong>✅ ${productCount} ürün bulundu</strong>
            </div>
            <p class="text-warning">Lokasyon bilgisi alınamadı. Tüm lokasyonlar kullanılacak.</p>
        `;
        selectedWarehouses = ['ALL'];
        return;
    }
    
    // Sort by stock (highest first)
    const locations = warehouses.sort((a, b) => (b.total_stock || 0) - (a.total_stock || 0));
    
    // Display
    let html = `
        <div class="alert alert-success mb-3">
            <strong>✅ ${productCount} ürün bulundu</strong>
            <button type="button" class="btn btn-sm btn-outline-light float-end" onclick="window.showAllProductsDetail()">
                <i class="fas fa-list"></i> Tüm Ürünleri Gör
            </button>
        </div>
        <h6 class="mb-3">📍 Lokasyon Seçimi (Stok Durumuna Göre Sıralı):</h6>
        <div class="list-group mb-3">
    `;
    
    locations.forEach((loc, index) => {
        const isHighest = index === 0;
        const code = loc.code || loc.warehouseAbbr || 'ALL';
        const name = loc.name || code;
        const stock = loc.total_stock || 0;
        const count = loc.product_count || 0;
        
        html += `
            <div class="list-group-item ${isHighest ? 'list-group-item-success' : ''}">
                <div class="d-flex align-items-center">
                    <div class="form-check flex-grow-1">
                        <input class="form-check-input" type="radio" 
                               name="selectedLocation" 
                               id="loc-${code}" 
                               value="${code}"
                               ${isHighest ? 'checked' : ''}
                               onchange="window.selectLocation('${code}')">
                        <label class="form-check-label" for="loc-${code}">
                            <strong>${name}</strong>
                            <small class="text-muted">(${code})</small>
                        </label>
                    </div>
                    <div class="d-flex align-items-center gap-2">
                        ${isHighest ? '<span class="badge bg-success">EN YÜKSEK STOK</span>' : ''}
                        <span class="badge bg-primary">${stock.toLocaleString()} adet</span>
                        <span class="badge bg-secondary">${count.toLocaleString()} SKU</span>
                        <button type="button" class="btn btn-sm btn-outline-info" 
                                onclick="window.showStockDetail('${code}', '${name}')"
                                title="Stok Detayları">
                            <i class="fas fa-info-circle"></i>
                        </button>
                    </div>
                </div>
            </div>
        `;
    });
    
    html += `
        </div>
        <div class="mt-3">
            <button class="btn btn-success btn-lg w-100" id="startSyncBtn">
                <i class="fas fa-rocket"></i> Aktarımı Başlat
            </button>
        </div>
    `;
    
    // Add modal HTML
    html += createStockDetailModal();
    
    container.innerHTML = html;
    
    // Attach event to start button
    document.getElementById('startSyncBtn').addEventListener('click', saveFiltersAndStart);
    
    // Auto-select highest
    if (locations.length > 0) {
        const highestCode = locations[0].code || locations[0].warehouseAbbr || 'ALL';
        selectLocation(highestCode);
    }
}

// Create stock detail modal HTML
function createStockDetailModal() {
    return `
        <div class="modal fade" id="stockDetailModal" tabindex="-1" aria-labelledby="stockDetailModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-xl modal-dialog-scrollable">
                <div class="modal-content">
                    <div class="modal-header bg-info text-white">
                        <h5 class="modal-title" id="stockDetailModalLabel">
                            <i class="fas fa-boxes"></i> Stok Detayları
                        </h5>
                        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body" id="stockDetailModalBody">
                        <p class="text-center text-muted">Yükleniyor...</p>
                    </div>
                    <div class="modal-footer">
                        <div class="me-auto" id="stockDetailSummary"></div>
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Kapat</button>
                    </div>
                </div>
            </div>
        </div>
    `;
}

// Show stock detail for a specific location
async function showStockDetail(locationCode, locationName) {
    const modal = new bootstrap.Modal(document.getElementById('stockDetailModal'));
    const modalBody = document.getElementById('stockDetailModalBody');
    const modalTitle = document.getElementById('stockDetailModalLabel');
    const modalSummary = document.getElementById('stockDetailSummary');
    
    modalTitle.innerHTML = `<i class="fas fa-boxes"></i> ${locationName} (${locationCode}) - Stok Detayları`;
    modalBody.innerHTML = '<div class="text-center py-4"><i class="fas fa-spinner fa-spin fa-2x"></i><p class="mt-2">Stok bilgileri yükleniyor...</p></div>';
    modalSummary.innerHTML = '';
    
    modal.show();
    
    try {
        // Fetch products for this specific location
        const ssAccountNumber = document.getElementById('ssAccountNumber').value;
        const ssApiKey = document.getElementById('ssApiKey').value;
        const syncOptions = window.getSyncOptions ? window.getSyncOptions() : {};
        
        // Add warehouse filter
        syncOptions.filter_warehouses = [locationCode];
        
        const response = await fetch('/api/preview', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                ss_account_number: ssAccountNumber,
                ss_api_key: ssApiKey,
                sync_options: syncOptions
            })
        });
        
        const data = await response.json();
        
        if (data.status === 'error') {
            modalBody.innerHTML = `<div class="alert alert-danger">${data.message || 'Hata oluştu'}</div>`;
            return;
        }
        
        const products = data.products || [];
        renderStockDetailTable(products, modalBody, modalSummary, locationCode);
        
    } catch (error) {
        modalBody.innerHTML = `<div class="alert alert-danger">Hata: ${error.message}</div>`;
    }
}

// Show all products detail
function showAllProductsDetail() {
    const modal = new bootstrap.Modal(document.getElementById('stockDetailModal'));
    const modalBody = document.getElementById('stockDetailModalBody');
    const modalTitle = document.getElementById('stockDetailModalLabel');
    const modalSummary = document.getElementById('stockDetailSummary');
    
    modalTitle.innerHTML = `<i class="fas fa-boxes"></i> Tüm Filtrelenmiş Ürünler`;
    
    if (!previewProducts || previewProducts.length === 0) {
        modalBody.innerHTML = '<div class="alert alert-warning">Ürün bulunamadı. Önce önizleme yapın.</div>';
        modal.show();
        return;
    }
    
    renderStockDetailTable(previewProducts, modalBody, modalSummary, 'ALL');
    modal.show();
}

// Render stock detail table
function renderStockDetailTable(products, container, summaryContainer, locationCode) {
    if (!products || products.length === 0) {
        container.innerHTML = '<div class="alert alert-warning">Bu lokasyonda filtrelere uygun ürün bulunamadı.</div>';
        summaryContainer.innerHTML = '';
        return;
    }
    
    // Group by style
    const styleGroups = {};
    let totalStock = 0;
    let totalSKUs = 0;
    
    products.forEach(p => {
        const styleId = p.styleID || 'unknown';
        const styleName = `${p.brandName || ''} ${p.styleName || ''}`.trim() || 'Bilinmeyen Stil';
        
        if (!styleGroups[styleId]) {
            styleGroups[styleId] = {
                styleId,
                styleName,
                brandName: p.brandName || '',
                products: []
            };
        }
        
        styleGroups[styleId].products.push(p);
        totalStock += (p.qty || 0);
        totalSKUs++;
    });
    
    // Build table
    let html = `
        <div class="mb-3">
            <input type="text" class="form-control" id="stockSearchInput" 
                   placeholder="🔍 SKU, Renk veya Beden ara..." 
                   onkeyup="window.filterStockTable()">
        </div>
        <div class="table-responsive" style="max-height: 500px; overflow-y: auto;">
            <table class="table table-sm table-hover table-striped" id="stockDetailTable">
                <thead class="table-dark sticky-top">
                    <tr>
                        <th style="width: 15%">SKU</th>
                        <th style="width: 25%">Ürün</th>
                        <th style="width: 15%">Renk</th>
                        <th style="width: 10%">Beden</th>
                        <th style="width: 10%" class="text-end">Stok</th>
                        <th style="width: 10%" class="text-end">Fiyat</th>
                    </tr>
                </thead>
                <tbody>
    `;
    
    // Sort styles by name
    const sortedStyles = Object.values(styleGroups).sort((a, b) => a.styleName.localeCompare(b.styleName));
    
    sortedStyles.forEach(style => {
        // Style header row
        const styleStock = style.products.reduce((sum, p) => sum + (p.qty || 0), 0);
        html += `
            <tr class="table-info">
                <td colspan="4">
                    <strong>${style.styleName}</strong>
                    <small class="text-muted">(Style ID: ${style.styleId})</small>
                </td>
                <td class="text-end"><strong>${styleStock.toLocaleString()}</strong></td>
                <td></td>
            </tr>
        `;
        
        // Sort products by color then size
        const sortedProducts = style.products.sort((a, b) => {
            const colorCmp = (a.colorName || '').localeCompare(b.colorName || '');
            if (colorCmp !== 0) return colorCmp;
            return (a.sizeOrder || a.sizeName || '').localeCompare(b.sizeOrder || b.sizeName || '');
        });
        
        sortedProducts.forEach(p => {
            const qty = p.qty || 0;
            const price = p.customerPrice || p.piecePrice || 0;
            const stockClass = qty > 100 ? 'text-success' : qty > 0 ? 'text-warning' : 'text-danger';
            
            html += `
                <tr data-sku="${p.sku || ''}" data-color="${(p.colorName || '').toLowerCase()}" data-size="${(p.sizeName || '').toLowerCase()}">
                    <td><code>${p.sku || '-'}</code></td>
                    <td class="text-truncate" style="max-width: 200px;" title="${style.styleName}">${style.styleName}</td>
                    <td>${p.colorName || '-'}</td>
                    <td>${p.sizeName || '-'}</td>
                    <td class="text-end ${stockClass}"><strong>${qty.toLocaleString()}</strong></td>
                    <td class="text-end">$${price.toFixed(2)}</td>
                </tr>
            `;
        });
    });
    
    html += `
                </tbody>
            </table>
        </div>
    `;
    
    container.innerHTML = html;
    
    // Summary
    summaryContainer.innerHTML = `
        <span class="badge bg-primary me-2">${totalSKUs.toLocaleString()} SKU</span>
        <span class="badge bg-success me-2">${totalStock.toLocaleString()} Toplam Stok</span>
        <span class="badge bg-info">${Object.keys(styleGroups).length} Stil</span>
    `;
}

// Filter stock table
function filterStockTable() {
    const searchInput = document.getElementById('stockSearchInput');
    const filter = searchInput ? searchInput.value.toLowerCase() : '';
    const table = document.getElementById('stockDetailTable');
    
    if (!table) return;
    
    const rows = table.getElementsByTagName('tr');
    
    for (let i = 1; i < rows.length; i++) { // Skip header
        const row = rows[i];
        
        // Skip style header rows
        if (row.classList.contains('table-info')) {
            row.style.display = '';
            continue;
        }
        
        const sku = row.getAttribute('data-sku') || '';
        const color = row.getAttribute('data-color') || '';
        const size = row.getAttribute('data-size') || '';
        const text = row.textContent.toLowerCase();
        
        if (filter === '' || sku.includes(filter) || color.includes(filter) || size.includes(filter) || text.includes(filter)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    }
}

function selectLocation(code) {
    selectedWarehouses = [code];
    console.log('Selected location:', code);
}

function saveFiltersAndStart() {
    if (selectedWarehouses.length === 0) {
        alert('Lütfen bir lokasyon seçin');
        return;
    }
    
    // Save filters and start sync
    if (window.saveFilters) {
        window.saveFilters();
    }
    
    // Start sync
    setTimeout(() => {
        if (window.startSync) {
            window.startSync();
        }
    }, 500);
}

// CRITICAL: Export ALL functions to window DIRECTLY (no if block)
window.loadWarehouses = loadWarehouses;
window.getSelectedWarehouses = getSelectedWarehouses;
window.loadPreviewWithLocations = loadPreviewWithLocations;
window.selectLocation = selectLocation;
window.saveFiltersAndStart = saveFiltersAndStart;
window.toggleWarehouse = toggleWarehouse;
window.displayWarehouses = displayWarehouses;
window.displayPreviewWithLocations = displayPreviewWithLocations;
window.showStockDetail = showStockDetail;
window.showAllProductsDetail = showAllProductsDetail;
window.filterStockTable = filterStockTable;

console.log('✅ Warehouse UI functions exported to window');

// Attach event listeners after DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    const previewBtn = document.getElementById('loadPreviewBtn');
    if (previewBtn) {
        previewBtn.addEventListener('click', loadPreviewWithLocations);
        console.log('✅ Preview button listener attached');
    }
});

