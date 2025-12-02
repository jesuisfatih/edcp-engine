// Warehouse selection UI functions

let selectedWarehouses = [];
let warehousesData = [];

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
}

function getSelectedWarehouses() {
    return selectedWarehouses;
}

// Export for use in main script
window.loadWarehouses = loadWarehouses;
window.getSelectedWarehouses = getSelectedWarehouses;

