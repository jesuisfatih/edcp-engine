// Global variables
let statusPollInterval = null;
let currentProductPollInterval = null;

// Load on page ready
document.addEventListener('DOMContentLoaded', function() {
    loadConfiguration();
    startStatusPolling();
    loadAutoSyncStatus();
    showSection('dashboard');
});

// Section navigation
function showSection(sectionName) {
    // Hide all sections
    document.querySelectorAll('.content-section').forEach(section => {
        section.classList.remove('active');
    });
    
    // Show selected section
    const section = document.getElementById(`section-${sectionName}`);
    if (section) {
        section.classList.add('active');
    }
    
    // Update menu
    document.querySelectorAll('.sidebar-menu a').forEach(link => {
        link.classList.remove('active');
    });
    const menuItem = document.getElementById(`menu-${sectionName}`);
    if (menuItem) {
        menuItem.classList.add('active');
    }
    
    // Load section-specific data
    if (sectionName === 'auto-sync') {
        loadAutoSyncStatus();
    }
}

// Load configuration
async function loadConfiguration() {
    try {
        const response = await fetch('/api/config');
        const data = await response.json();
        
        if (data.ss_config) {
            document.getElementById('ssAccountNumber').value = data.ss_config.account_number || '';
            document.getElementById('ssApiKey').value = data.ss_config.api_key || '';
        }
        
        if (data.shopify_config) {
            document.getElementById('shopifyDomain').value = data.shopify_config.shop_domain || '';
            document.getElementById('shopifyToken').value = data.shopify_config.access_token || '';
        }
        
        if (data.sync_options) {
            // Load sync options
            if (document.getElementById('syncAllProducts')) {
                document.getElementById('syncAllProducts').checked = data.sync_options.sync_all_products !== false;
                document.getElementById('createNew').checked = data.sync_options.create_new !== false;
                document.getElementById('updateExisting').checked = data.sync_options.update_existing !== false;
                document.getElementById('syncCollections').checked = data.sync_options.sync_collections !== false;
                document.getElementById('createCollections').checked = data.sync_options.create_collections !== false;
                document.getElementById('createBrandCollections').checked = data.sync_options.create_brand_collections !== false;
                document.getElementById('syncTags').checked = data.sync_options.sync_tags !== false;
                document.getElementById('setActive').checked = data.sync_options.set_active !== false;
                document.getElementById('filterStyle').value = data.sync_options.filter_style || '';
                document.getElementById('filterPartNumber').value = data.sync_options.filter_partnumber || '';
                document.getElementById('filterBrand').value = data.sync_options.filter_brand || '';
            }
        }
    } catch (error) {
        console.error('Failed to load configuration:', error);
    }
}

// Save configuration
document.getElementById('configForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value,
        shopify_domain: document.getElementById('shopifyDomain').value,
        shopify_token: document.getElementById('shopifyToken').value,
        sync_options: getSyncOptions()
    };
    
    try {
        const response = await fetch('/api/config', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        showAlert(result.status === 'success' ? 'Configuration saved!' : 'Failed to save', 
                  result.status === 'success' ? 'success' : 'danger');
    } catch (error) {
        showAlert('Error: ' + error.message, 'danger');
    }
});

// Get sync options
function getSyncOptions() {
    const categorySelect = document.getElementById('filterCategory');
    const selectedCategories = categorySelect ? 
        Array.from(categorySelect.selectedOptions).map(opt => opt.value).filter(v => v) : [];
    
    return {
        sync_all_products: document.getElementById('syncAllProducts')?.checked ?? true,
        create_new: document.getElementById('createNew')?.checked ?? true,
        update_existing: document.getElementById('updateExisting')?.checked ?? true,
        sync_collections: document.getElementById('syncCollections')?.checked ?? true,
        create_collections: document.getElementById('createCollections')?.checked ?? true,
        create_brand_collections: document.getElementById('createBrandCollections')?.checked ?? true,
        sync_tags: document.getElementById('syncTags')?.checked ?? true,
        set_active: document.getElementById('setActive')?.checked ?? true,
        filter_style: document.getElementById('filterStyle')?.value.trim() || null,
        filter_partnumber: document.getElementById('filterPartNumber')?.value.trim() || null,
        filter_brand: document.getElementById('filterBrand')?.value.trim() || null,
        filter_categories: selectedCategories.length > 0 ? selectedCategories : null,
        filter_warehouses: document.getElementById('filterWarehouses')?.value.trim() || null,
        filter_sku: document.getElementById('filterSku')?.value.trim() || null,
        price_field: document.getElementById('priceField')?.value || 'customerPrice',
        inventory_management: document.getElementById('inventoryManagement')?.value || 'shopify',
        image_size: document.getElementById('imageSize')?.value || '_fl',
        update_inventory: document.getElementById('updateInventory')?.checked ?? true,
        update_prices: document.getElementById('updatePrices')?.checked ?? true,
        update_images: document.getElementById('updateImages')?.checked ?? true
    };
}

// Test connections
async function testConnections() {
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value,
        shopify_domain: document.getElementById('shopifyDomain').value,
        shopify_token: document.getElementById('shopifyToken').value
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key || 
        !configData.shopify_domain || !configData.shopify_token) {
        showAlert('Please fill in all API credentials', 'warning');
        return;
    }
    
    showAlert('Testing connections...', 'info');
    
    try {
        const response = await fetch('/api/test-connection', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        const resultsDiv = document.getElementById('connectionResults');
        const resultsBody = document.getElementById('connectionResultsBody');
        
        let html = '';
        result.messages.forEach(msg => {
            const isSuccess = msg.includes('successfully') || msg.includes('Connected');
            html += `<div class="mb-2"><span class="badge ${isSuccess ? 'bg-success' : 'bg-danger'}">${msg}</span></div>`;
        });
        
        resultsBody.innerHTML = html;
        resultsDiv.style.display = 'block';
        
        showAlert(result.ss && result.shopify ? 'Both connections successful!' : 'One or more connections failed', 
                  result.ss && result.shopify ? 'success' : 'warning');
    } catch (error) {
        showAlert('Error: ' + error.message, 'danger');
    }
}

// Start sync
async function startSync() {
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value,
        shopify_domain: document.getElementById('shopifyDomain').value,
        shopify_token: document.getElementById('shopifyToken').value,
        sync_options: getSyncOptions()
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key || 
        !configData.shopify_domain || !configData.shopify_token) {
        showAlert('Please configure API credentials first', 'warning');
        return;
    }
    
    try {
        const response = await fetch('/api/sync/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            showAlert('Synchronization started!', 'success');
            document.getElementById('startBtn').disabled = true;
            document.getElementById('stopBtn').disabled = false;
            document.getElementById('progressSection').style.display = 'block';
            document.getElementById('currentProductCard').style.display = 'block';
            startCurrentProductPolling();
            showSection('sync-active');
        } else {
            showAlert('Failed to start: ' + result.message, 'danger');
        }
    } catch (error) {
        showAlert('Error: ' + error.message, 'danger');
    }
}

// Stop sync
async function stopSync() {
    try {
        const response = await fetch('/api/sync/stop', { method: 'POST' });
        const result = await response.json();
        
        if (result.status === 'success') {
            showAlert('Synchronization stopped', 'warning');
            document.getElementById('startBtn').disabled = false;
            document.getElementById('stopBtn').disabled = true;
        }
    } catch (error) {
        showAlert('Error: ' + error.message, 'danger');
    }
}

// Preview products
async function previewProducts() {
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key) {
        showAlert('Please configure S&S Activewear API credentials first', 'warning');
        return;
    }
    
    showAlert('Loading products preview...', 'info');
    
    try {
        const filterOptions = {
            style: document.getElementById('filterStyle')?.value.trim() || null,
            partnumber: document.getElementById('filterPartNumber')?.value.trim() || null,
            brand: document.getElementById('filterBrand')?.value.trim() || null,
            categories: Array.from(document.getElementById('filterCategory')?.selectedOptions || [])
                .map(opt => opt.value).filter(v => v)
        };
        
        const response = await fetch('/api/preview', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({...configData, filter_options: filterOptions})
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            displayPreview(result.products);
            showAlert(`Loaded ${result.count} products`, 'success');
            showSection('preview');
        } else {
            showAlert('Failed: ' + result.message, 'danger');
        }
    } catch (error) {
        showAlert('Error: ' + error.message, 'danger');
    }
}

// Display preview
function displayPreview(products) {
    const tbody = document.getElementById('previewTableBody');
    tbody.innerHTML = '';
    
    products.forEach(product => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${product.sku || 'N/A'}</td>
            <td>${product.brandName || 'N/A'}</td>
            <td>${product.styleName || 'N/A'}</td>
            <td>${product.colorName || 'N/A'}</td>
            <td>${product.sizeName || 'N/A'}</td>
            <td>$${product.customerPrice || product.piecePrice || '0.00'}</td>
            <td>${product.qty || 0}</td>
        `;
        tbody.appendChild(row);
    });
}

// Load categories
async function loadCategories() {
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key) {
        showAlert('Please configure S&S Activewear API credentials first', 'warning');
        return;
    }
    
    try {
        const response = await fetch('/api/categories', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            const categorySelect = document.getElementById('filterCategory');
            categorySelect.innerHTML = '';
            
            result.categories.forEach(category => {
                const option = document.createElement('option');
                option.value = category.categoryID;
                option.textContent = `${category.name} (ID: ${category.categoryID})`;
                categorySelect.appendChild(option);
            });
            
            showAlert(`Loaded ${result.categories.length} categories`, 'success');
        } else {
            showAlert('Failed: ' + result.message, 'danger');
        }
    } catch (error) {
        showAlert('Error: ' + error.message, 'danger');
    }
}

// Status polling
function startStatusPolling() {
    if (statusPollInterval) clearInterval(statusPollInterval);
    
    statusPollInterval = setInterval(async () => {
        try {
            const response = await fetch('/api/sync/status');
            const status = await response.json();
            
            if (status.status !== 'idle') {
                updateSyncStatus(status);
            }
        } catch (error) {
            console.error('Status poll error:', error);
        }
    }, 2000);
}

// Update sync status
function updateSyncStatus(status) {
    // Update progress
    const progressBar = document.getElementById('progressBar');
    const progressPercent = document.getElementById('progressPercent');
    const progressText = document.getElementById('progressText');
    
    if (progressBar) {
        progressBar.style.width = status.progress + '%';
        progressBar.textContent = status.progress + '%';
    }
    if (progressPercent) progressPercent.textContent = status.progress + '%';
    if (progressText) progressText.textContent = status.message || 'Processing...';
    
    // Update stats
    if (status.stats) {
        updateElement('statTotal', status.stats.total || 0);
        updateElement('statCreated', status.stats.created || 0);
        updateElement('statUpdated', status.stats.updated || 0);
        updateElement('statErrors', status.stats.errors || 0);
        updateElement('statTotalActive', status.stats.total || 0);
        updateElement('statCreatedActive', status.stats.created || 0);
        updateElement('statUpdatedActive', status.stats.updated || 0);
        updateElement('statErrorsActive', status.stats.errors || 0);
    }
    
    // Update buttons
    if (status.status === 'completed' || status.status === 'error') {
        if (document.getElementById('startBtn')) document.getElementById('startBtn').disabled = false;
        if (document.getElementById('stopBtn')) document.getElementById('stopBtn').disabled = true;
    }
    
    // Display errors
    if (status.errors && status.errors.length > 0) {
        displayErrors(status.errors);
    }
}

// Current product polling
function startCurrentProductPolling() {
    if (currentProductPollInterval) clearInterval(currentProductPollInterval);
    
    currentProductPollInterval = setInterval(async () => {
        try {
            const response = await fetch('/api/sync/current-product');
            const data = await response.json();
            
            if (data.status === 'success' && data.current_product) {
                const product = data.current_product;
                const infoDiv = document.getElementById('currentProductInfo');
                infoDiv.innerHTML = `
                    <h6>${product.brandName || ''} ${product.styleName || ''} ${product.colorName || ''}</h6>
                    <p><strong>SKU:</strong> ${product.sku || 'N/A'}</p>
                    <p><strong>Beden:</strong> ${product.sizeName || 'N/A'}</p>
                    <p><strong>Fiyat:</strong> $${product.customerPrice || product.piecePrice || '0.00'}</p>
                    <p><strong>Stok:</strong> ${product.qty || 0}</p>
                    <p class="text-muted">${data.current_index + 1} / ${data.total}</p>
                `;
            }
        } catch (error) {
            console.error('Current product poll error:', error);
        }
    }, 1000);
}

// Auto sync functions
async function loadAutoSyncStatus() {
    try {
        const response = await fetch('/api/auto-sync/status');
        const status = await response.json();
        
        document.getElementById('autoSyncEnabled').checked = status.enabled;
        document.getElementById('autoSyncInterval').value = status.interval_hours || 12;
        document.getElementById('autoSyncRequireApproval').checked = status.require_approval;
        
        const statusDiv = document.getElementById('autoSyncStatus');
        let html = `<p><strong>Durum:</strong> ${status.enabled ? 'Aktif' : 'Pasif'}</p>`;
        if (status.last_run) {
            html += `<p><strong>Son Çalışma:</strong> ${new Date(status.last_run).toLocaleString()}</p>`;
        }
        if (status.next_run) {
            html += `<p><strong>Sonraki Çalışma:</strong> ${new Date(status.next_run).toLocaleString()}</p>`;
        }
        statusDiv.innerHTML = html;
        
        // Show pending approval card
        const pendingCard = document.getElementById('pendingApprovalCard');
        if (status.pending_approval) {
            pendingCard.style.display = 'block';
        } else {
            pendingCard.style.display = 'none';
        }
    } catch (error) {
        console.error('Auto sync status error:', error);
    }
}

async function saveAutoSyncSettings() {
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value,
        shopify_domain: document.getElementById('shopifyDomain').value,
        shopify_token: document.getElementById('shopifyToken').value,
        sync_options: getSyncOptions(),
        require_approval: document.getElementById('autoSyncRequireApproval').checked,
        interval_hours: parseInt(document.getElementById('autoSyncInterval').value)
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key || 
        !configData.shopify_domain || !configData.shopify_token) {
        showAlert('Please configure API credentials first', 'warning');
        return;
    }
    
    if (document.getElementById('autoSyncEnabled').checked) {
        try {
            const response = await fetch('/api/auto-sync/start', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(configData)
            });
            
            const result = await response.json();
            showAlert(result.status === 'success' ? 'Auto sync started!' : result.message, 
                      result.status === 'success' ? 'success' : 'danger');
            loadAutoSyncStatus();
        } catch (error) {
            showAlert('Error: ' + error.message, 'danger');
        }
    } else {
        try {
            await fetch('/api/auto-sync/stop', { method: 'POST' });
            showAlert('Auto sync stopped', 'info');
            loadAutoSyncStatus();
        } catch (error) {
            showAlert('Error: ' + error.message, 'danger');
        }
    }
}

async function approveAutoSync() {
    try {
        const response = await fetch('/api/auto-sync/approve', { method: 'POST' });
        const result = await response.json();
        showAlert(result.message, result.status === 'success' ? 'success' : 'danger');
        loadAutoSyncStatus();
    } catch (error) {
        showAlert('Error: ' + error.message, 'danger');
    }
}

function rejectAutoSync() {
    // Just reload status, which will clear pending approval after timeout
    loadAutoSyncStatus();
}

// Display errors
function displayErrors(errors) {
    const tbody = document.getElementById('errorLogBody');
    const errorDiv = document.getElementById('errorLog');
    
    if (tbody) {
        tbody.innerHTML = '';
        errors.forEach(error => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${error.sku || 'N/A'}</td>
                <td>${error.error}</td>
                <td>${error.timestamp ? new Date(error.timestamp).toLocaleString() : 'N/A'}</td>
            `;
            tbody.appendChild(row);
        });
    }
    
    if (errorDiv) errorDiv.style.display = 'block';
}

// Helper functions
function updateElement(id, value) {
    const el = document.getElementById(id);
    if (el) el.textContent = value;
}

function showAlert(message, type) {
    const alertDiv = document.getElementById('statusAlert');
    if (alertDiv) {
        alertDiv.className = `alert alert-${type}`;
        const msgSpan = alertDiv.querySelector('#statusMessage');
        if (msgSpan) msgSpan.textContent = message;
        alertDiv.style.display = 'block';
        
        setTimeout(() => {
            if (type !== 'info') {
                alertDiv.style.display = 'none';
            }
        }, 5000);
    } else {
        alert(message);
    }
}


