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
        
        const productCount = previewData.count || 0;
        const warehouses = warehouseData.warehouses || [];
        
        displayPreviewWithLocations(productCount, warehouses);
        
    } catch (error) {
        alert('Hata: ' + error.message);
        console.error('Preview error:', error);
    }
}

function displayPreviewWithLocations(productCount, warehouses) {
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
                <div class="form-check">
                    <input class="form-check-input" type="radio" 
                           name="selectedLocation" 
                           id="loc-${code}" 
                           value="${code}"
                           ${isHighest ? 'checked' : ''}
                           onchange="window.selectLocation('${code}')">
                    <label class="form-check-label d-flex justify-content-between w-100" for="loc-${code}">
                        <span>
                            <strong>${name}</strong>
                            <small class="text-muted">(${code})</small>
                            ${isHighest ? '<span class="badge bg-success ms-2">EN YÜKSEK STOK</span>' : ''}
                        </span>
                        <span>
                            <span class="badge bg-primary">${stock.toLocaleString()} adet</span>
                            <span class="badge bg-secondary ms-1">${count.toLocaleString()} SKU</span>
                        </span>
                    </label>
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
    
    container.innerHTML = html;
    
    // Attach event to start button
    document.getElementById('startSyncBtn').addEventListener('click', saveFiltersAndStart);
    
    // Auto-select highest
    if (locations.length > 0) {
        const highestCode = locations[0].code || locations[0].warehouseAbbr || 'ALL';
        selectLocation(highestCode);
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

console.log('✅ Warehouse UI functions exported to window');

// Attach event listeners after DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    const previewBtn = document.getElementById('loadPreviewBtn');
    if (previewBtn) {
        previewBtn.addEventListener('click', loadPreviewWithLocations);
        console.log('✅ Preview button listener attached');
    }
});

