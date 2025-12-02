// Warehouse selection UI functions

let selectedWarehouses = [];
let warehousesData = [];

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
        // Get current filter selections
        const ssAccountNumber = document.getElementById('ssAccountNumber').value;
        const ssApiKey = document.getElementById('ssApiKey').value;
        
        if (!ssAccountNumber || !ssApiKey) {
            alert('S&S bilgileri eksik');
            return;
        }
        
        const syncOptions = window.getSyncOptions ? window.getSyncOptions() : {};
        
        // Call preview API
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
        
        if (data.status === 'success') {
            displayPreviewWithLocations(data.products || []);
        } else {
            alert('Önizleme yüklenemedi: ' + data.message);
        }
    } catch (error) {
        alert('Hata: ' + error.message);
    }
}

function displayPreviewWithLocations(products) {
    const container = document.getElementById('previewWithLocations');
    
    if (!products || products.length === 0) {
        container.innerHTML = '<p class="text-warning">Seçilen filtrelere uygun ürün bulunamadı</p>';
        return;
    }
    
    // Group by warehouse/location
    const locationStock = {};
    
    products.forEach(p => {
        const warehouse = p.warehouse || p.warehouseCode || p.location || 'ALL';
        const qty = p.qty || 0;
        
        if (!locationStock[warehouse]) {
            locationStock[warehouse] = {
                code: warehouse,
                total_stock: 0,
                product_count: 0
            };
        }
        
        locationStock[warehouse].total_stock += qty;
        locationStock[warehouse].product_count += 1;
    });
    
    // Sort by stock
    const locations = Object.values(locationStock).sort((a, b) => b.total_stock - a.total_stock);
    
    // Display
    let html = `
        <div class="alert alert-success">
            <strong>✅ ${products.length} ürün bulundu</strong>
        </div>
        <h6>Lokasyon Bazlı Stok Durumu:</h6>
        <div class="list-group">
    `;
    
    locations.forEach((loc, index) => {
        const isHighest = index === 0;
        html += `
            <div class="list-group-item ${isHighest ? 'list-group-item-success' : ''}">
                <div class="form-check">
                    <input class="form-check-input" type="radio" 
                           name="selectedLocation" 
                           id="loc-${loc.code}" 
                           value="${loc.code}"
                           ${isHighest && document.getElementById('autoSelectHighestStock')?.checked ? 'checked' : ''}
                           onchange="selectLocation('${loc.code}')">
                    <label class="form-check-label d-flex justify-content-between" for="loc-${loc.code}">
                        <span>
                            <strong>${loc.code}</strong>
                            ${isHighest ? '<span class="badge bg-success ms-2">EN YÜKSEK STOK</span>' : ''}
                        </span>
                        <span>
                            <span class="badge bg-primary">${loc.total_stock.toLocaleString()} adet</span>
                            <span class="badge bg-secondary ms-1">${loc.product_count} ürün</span>
                        </span>
                    </label>
                </div>
            </div>
        `;
    });
    
    html += `
        </div>
        <div class="mt-3">
            <button class="btn btn-success btn-lg w-100" onclick="saveFiltersAndStart()">
                <i class="fas fa-save"></i> Kaydet ve Aktarımı Başlat
            </button>
        </div>
    `;
    
    container.innerHTML = html;
    
    // Auto-select highest if enabled
    if (locations.length > 0 && document.getElementById('autoSelectHighestStock')?.checked) {
        selectLocation(locations[0].code);
    }
    
    document.getElementById('locationSelectionSection')?.style.display = 'block';
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

console.log('✅ Warehouse UI functions exported to window');

