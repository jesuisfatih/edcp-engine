// Warehouse selection UI functions

let selectedWarehouses = [];
let warehousesData = [];
let warehousePreviewProducts = []; // Store preview products for stock detail modal

// Arbitraj (pricing) settings
let arbitrajSettings = {
    enabled: false,
    markupPercent: 100,  // 100% = 2x price (default)
    roundingType: 'none', // 'none', '99', '90', '00'
    fixedPrice: null,     // null = use markup, number = fixed price
    minimumPrice: null    // minimum price floor
};

// Immediately export to window
if (typeof window !== 'undefined') {
    window.selectedWarehouses = selectedWarehouses;
    window.arbitrajSettings = arbitrajSettings;
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
        warehousePreviewProducts = previewData.products || [];
        console.log('Preview products stored:', warehousePreviewProducts.length);
        
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
        const isSelected = isHighest; // Initially highest is selected
        
        html += `
            <div class="list-group-item ${isHighest ? 'list-group-item-success' : ''}" id="loc-item-${code}">
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
                        <!-- Arbitraj Button - only visible when selected -->
                        <button type="button" class="btn btn-sm btn-warning arbitraj-btn" 
                                id="arbitraj-btn-${code}"
                                onclick="window.showArbitrajModal('${code}', '${name}')"
                                title="Fiyat Arbitrajı Ayarla"
                                style="${isSelected ? '' : 'display:none;'}">
                            <i class="fas fa-tags"></i> Fiyat Ayarı
                        </button>
                    </div>
                </div>
                <!-- Arbitraj indicator when enabled -->
                <div class="arbitraj-indicator mt-2" id="arbitraj-indicator-${code}" style="display:none;">
                    <small class="text-warning">
                        <i class="fas fa-calculator"></i> 
                        <span id="arbitraj-summary-${code}"></span>
                    </small>
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
    
    if (!warehousePreviewProducts || warehousePreviewProducts.length === 0) {
        modalBody.innerHTML = '<div class="alert alert-warning">Ürün bulunamadı. Önce önizleme yapın.</div>';
        modal.show();
        return;
    }
    
    renderStockDetailTable(warehousePreviewProducts, modalBody, modalSummary, 'ALL');
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
    
    // Hide all arbitraj buttons, show only selected one
    document.querySelectorAll('.arbitraj-btn').forEach(btn => {
        btn.style.display = 'none';
    });
    const selectedBtn = document.getElementById(`arbitraj-btn-${code}`);
    if (selectedBtn) {
        selectedBtn.style.display = '';
    }
    
    // Update list item styling
    document.querySelectorAll('.list-group-item').forEach(item => {
        item.classList.remove('list-group-item-success');
    });
    const selectedItem = document.getElementById(`loc-item-${code}`);
    if (selectedItem) {
        selectedItem.classList.add('list-group-item-success');
    }
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

// ==================== ARBITRAJ (PRICING) FUNCTIONS ====================

// Create arbitraj modal HTML
function createArbitrajModal() {
    return `
        <div class="modal fade" id="arbitrajModal" tabindex="-1" aria-labelledby="arbitrajModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header bg-warning">
                        <h5 class="modal-title" id="arbitrajModalLabel">
                            <i class="fas fa-tags"></i> Fiyat Arbitrajı Ayarları
                        </h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="alert alert-info mb-3">
                            <i class="fas fa-info-circle"></i>
                            <strong>Lokasyon:</strong> <span id="arbitrajLocationName"></span>
                        </div>
                        
                        <!-- Enable/Disable -->
                        <div class="form-check form-switch mb-4">
                            <input class="form-check-input" type="checkbox" id="arbitrajEnabled">
                            <label class="form-check-label" for="arbitrajEnabled">
                                <strong>Fiyat Arbitrajını Etkinleştir</strong>
                            </label>
                        </div>
                        
                        <div id="arbitrajOptions">
                            <!-- Pricing Mode -->
                            <div class="mb-3">
                                <label class="form-label"><strong>Fiyatlandırma Modu</strong></label>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="pricingMode" id="modeMarkup" value="markup" checked>
                                    <label class="form-check-label" for="modeMarkup">
                                        Kar Marjı ile Hesapla
                                    </label>
                                </div>
                                <div class="form-check">
                                    <input class="form-check-input" type="radio" name="pricingMode" id="modeFixed" value="fixed">
                                    <label class="form-check-label" for="modeFixed">
                                        Sabit Fiyat Uygula
                                    </label>
                                </div>
                            </div>
                            
                            <!-- Markup Settings -->
                            <div id="markupSettings" class="border rounded p-3 mb-3">
                                <label class="form-label">Kar Marjı (%)</label>
                                <div class="input-group mb-2">
                                    <span class="input-group-text">%</span>
                                    <input type="number" class="form-control" id="markupPercent" value="100" min="0" max="1000">
                                    <span class="input-group-text">kar</span>
                                </div>
                                <small class="text-muted">
                                    Örnek: %100 = 2x fiyat, %50 = 1.5x fiyat, %150 = 2.5x fiyat
                                </small>
                                <div class="mt-2 p-2 bg-light rounded">
                                    <strong>Önizleme:</strong> $10 maliyet → <span id="markupPreview">$20.00</span> satış
                                </div>
                            </div>
                            
                            <!-- Fixed Price Settings -->
                            <div id="fixedSettings" class="border rounded p-3 mb-3" style="display:none;">
                                <label class="form-label">Sabit Fiyat</label>
                                <div class="input-group">
                                    <span class="input-group-text">$</span>
                                    <input type="number" class="form-control" id="fixedPrice" value="0" min="0" step="0.01">
                                </div>
                                <small class="text-muted">Tüm ürünler bu fiyattan satılacak</small>
                            </div>
                            
                            <!-- Rounding Options -->
                            <div class="mb-3">
                                <label class="form-label"><strong>Yuvarlama</strong></label>
                                <div class="btn-group w-100" role="group">
                                    <input type="radio" class="btn-check" name="rounding" id="roundNone" value="none" checked>
                                    <label class="btn btn-outline-secondary" for="roundNone">Yok</label>
                                    
                                    <input type="radio" class="btn-check" name="rounding" id="round99" value="99">
                                    <label class="btn btn-outline-secondary" for="round99">.99</label>
                                    
                                    <input type="radio" class="btn-check" name="rounding" id="round90" value="90">
                                    <label class="btn btn-outline-secondary" for="round90">.90</label>
                                    
                                    <input type="radio" class="btn-check" name="rounding" id="round00" value="00">
                                    <label class="btn btn-outline-secondary" for="round00">.00</label>
                                </div>
                                <small class="text-muted d-block mt-1">
                                    Örnek: $23.47 → .99 = $23.99, .90 = $23.90, .00 = $24.00
                                </small>
                            </div>
                            
                            <!-- Minimum Price -->
                            <div class="mb-3">
                                <label class="form-label"><strong>Minimum Fiyat (Opsiyonel)</strong></label>
                                <div class="input-group">
                                    <span class="input-group-text">$</span>
                                    <input type="number" class="form-control" id="minimumPrice" value="" min="0" step="0.01" placeholder="Boş = sınırsız">
                                </div>
                                <small class="text-muted">Hesaplanan fiyat bunun altına düşmez</small>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">İptal</button>
                        <button type="button" class="btn btn-warning" onclick="window.saveArbitrajSettings()">
                            <i class="fas fa-save"></i> Kaydet
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;
}

// Show arbitraj modal
function showArbitrajModal(locationCode, locationName) {
    // Ensure modal exists
    if (!document.getElementById('arbitrajModal')) {
        document.body.insertAdjacentHTML('beforeend', createArbitrajModal());
        setupArbitrajListeners();
    }
    
    // Set location name
    document.getElementById('arbitrajLocationName').textContent = `${locationName} (${locationCode})`;
    
    // Load current settings
    document.getElementById('arbitrajEnabled').checked = arbitrajSettings.enabled;
    document.getElementById('markupPercent').value = arbitrajSettings.markupPercent;
    document.getElementById('fixedPrice').value = arbitrajSettings.fixedPrice || '';
    document.getElementById('minimumPrice').value = arbitrajSettings.minimumPrice || '';
    
    // Set pricing mode
    if (arbitrajSettings.fixedPrice !== null) {
        document.getElementById('modeFixed').checked = true;
        document.getElementById('markupSettings').style.display = 'none';
        document.getElementById('fixedSettings').style.display = 'block';
    } else {
        document.getElementById('modeMarkup').checked = true;
        document.getElementById('markupSettings').style.display = 'block';
        document.getElementById('fixedSettings').style.display = 'none';
    }
    
    // Set rounding
    const roundingRadio = document.querySelector(`input[name="rounding"][value="${arbitrajSettings.roundingType}"]`);
    if (roundingRadio) roundingRadio.checked = true;
    
    // Update preview
    updateMarkupPreview();
    
    // Show modal
    const modal = new bootstrap.Modal(document.getElementById('arbitrajModal'));
    modal.show();
}

// Setup arbitraj modal event listeners
function setupArbitrajListeners() {
    // Pricing mode toggle
    document.querySelectorAll('input[name="pricingMode"]').forEach(radio => {
        radio.addEventListener('change', function() {
            if (this.value === 'markup') {
                document.getElementById('markupSettings').style.display = 'block';
                document.getElementById('fixedSettings').style.display = 'none';
            } else {
                document.getElementById('markupSettings').style.display = 'none';
                document.getElementById('fixedSettings').style.display = 'block';
            }
        });
    });
    
    // Markup preview update
    document.getElementById('markupPercent').addEventListener('input', updateMarkupPreview);
    document.querySelectorAll('input[name="rounding"]').forEach(radio => {
        radio.addEventListener('change', updateMarkupPreview);
    });
}

// Update markup preview
function updateMarkupPreview() {
    const markup = parseFloat(document.getElementById('markupPercent').value) || 0;
    const rounding = document.querySelector('input[name="rounding"]:checked')?.value || 'none';
    
    let price = 10 * (1 + markup / 100);
    price = applyRounding(price, rounding);
    
    document.getElementById('markupPreview').textContent = `$${price.toFixed(2)}`;
}

// Apply rounding to price
function applyRounding(price, roundingType) {
    switch (roundingType) {
        case '99':
            return Math.floor(price) + 0.99;
        case '90':
            return Math.floor(price) + 0.90;
        case '00':
            return Math.ceil(price);
        default:
            return price;
    }
}

// Save arbitraj settings
function saveArbitrajSettings() {
    arbitrajSettings.enabled = document.getElementById('arbitrajEnabled').checked;
    arbitrajSettings.markupPercent = parseFloat(document.getElementById('markupPercent').value) || 0;
    arbitrajSettings.roundingType = document.querySelector('input[name="rounding"]:checked')?.value || 'none';
    
    const pricingMode = document.querySelector('input[name="pricingMode"]:checked')?.value;
    if (pricingMode === 'fixed') {
        arbitrajSettings.fixedPrice = parseFloat(document.getElementById('fixedPrice').value) || null;
    } else {
        arbitrajSettings.fixedPrice = null;
    }
    
    const minPrice = document.getElementById('minimumPrice').value;
    arbitrajSettings.minimumPrice = minPrice ? parseFloat(minPrice) : null;
    
    console.log('Arbitraj settings saved:', arbitrajSettings);
    
    // Update indicator on selected location
    updateArbitrajIndicator();
    
    // Close modal
    bootstrap.Modal.getInstance(document.getElementById('arbitrajModal')).hide();
    
    // Show confirmation
    showArbitrajConfirmation();
}

// Update arbitraj indicator on location
function updateArbitrajIndicator() {
    const code = selectedWarehouses[0];
    if (!code) return;
    
    const indicator = document.getElementById(`arbitraj-indicator-${code}`);
    const summary = document.getElementById(`arbitraj-summary-${code}`);
    const btn = document.getElementById(`arbitraj-btn-${code}`);
    
    if (arbitrajSettings.enabled) {
        let summaryText = '';
        if (arbitrajSettings.fixedPrice !== null) {
            summaryText = `Sabit Fiyat: $${arbitrajSettings.fixedPrice.toFixed(2)}`;
        } else {
            summaryText = `+%${arbitrajSettings.markupPercent} kar`;
        }
        
        if (arbitrajSettings.roundingType !== 'none') {
            summaryText += ` | .${arbitrajSettings.roundingType} yuvarlama`;
        }
        
        if (arbitrajSettings.minimumPrice) {
            summaryText += ` | Min: $${arbitrajSettings.minimumPrice.toFixed(2)}`;
        }
        
        if (indicator) {
            indicator.style.display = 'block';
            summary.textContent = summaryText;
        }
        
        if (btn) {
            btn.classList.remove('btn-warning');
            btn.classList.add('btn-success');
            btn.innerHTML = '<i class="fas fa-check"></i> Fiyat Ayarlı';
        }
    } else {
        if (indicator) {
            indicator.style.display = 'none';
        }
        if (btn) {
            btn.classList.remove('btn-success');
            btn.classList.add('btn-warning');
            btn.innerHTML = '<i class="fas fa-tags"></i> Fiyat Ayarı';
        }
    }
}

// Show confirmation toast
function showArbitrajConfirmation() {
    const message = arbitrajSettings.enabled 
        ? '✅ Fiyat arbitrajı ayarları kaydedildi. Aktarım sırasında uygulanacak.'
        : 'Fiyat arbitrajı devre dışı.';
    
    // Simple alert for now
    const alertDiv = document.createElement('div');
    alertDiv.className = 'alert alert-success alert-dismissible fade show position-fixed';
    alertDiv.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(alertDiv);
    
    setTimeout(() => alertDiv.remove(), 3000);
}

// Get arbitraj settings for sync
function getArbitrajSettings() {
    return arbitrajSettings;
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
// Arbitraj functions
window.showArbitrajModal = showArbitrajModal;
window.saveArbitrajSettings = saveArbitrajSettings;
window.getArbitrajSettings = getArbitrajSettings;
window.arbitrajSettings = arbitrajSettings;

console.log('✅ Warehouse UI functions exported to window');

// Attach event listeners after DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    const previewBtn = document.getElementById('loadPreviewBtn');
    if (previewBtn) {
        previewBtn.addEventListener('click', loadPreviewWithLocations);
        console.log('✅ Preview button listener attached');
    }
});

