// Load saved configuration on page load
document.addEventListener('DOMContentLoaded', function() {
    loadConfiguration();
    startStatusPolling();
});

// Load configuration from server
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
            
            // Load categories if saved
            if (data.sync_options.filter_categories) {
                const categorySelect = document.getElementById('filterCategory');
                const selectedCategories = Array.isArray(data.sync_options.filter_categories) 
                    ? data.sync_options.filter_categories 
                    : [data.sync_options.filter_categories];
                Array.from(categorySelect.options).forEach(option => {
                    if (selectedCategories.includes(option.value)) {
                        option.selected = true;
                    }
                });
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
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            showAlert('Configuration saved successfully!', 'success');
        } else {
            showAlert('Failed to save configuration', 'danger');
        }
    } catch (error) {
        showAlert('Error saving configuration: ' + error.message, 'danger');
    }
});

// Get sync options from form
function getSyncOptions() {
    const categorySelect = document.getElementById('filterCategory');
    const selectedCategories = Array.from(categorySelect.selectedOptions).map(opt => opt.value).filter(v => v);
    
    return {
        sync_all_products: document.getElementById('syncAllProducts').checked,
        create_new: document.getElementById('createNew').checked,
        update_existing: document.getElementById('updateExisting').checked,
        sync_collections: document.getElementById('syncCollections').checked,
        create_collections: document.getElementById('createCollections').checked,
        create_brand_collections: document.getElementById('createBrandCollections').checked,
        sync_tags: document.getElementById('syncTags').checked,
        set_active: document.getElementById('setActive').checked,
        filter_style: document.getElementById('filterStyle').value.trim() || null,
        filter_partnumber: document.getElementById('filterPartNumber').value.trim() || null,
        filter_brand: document.getElementById('filterBrand').value.trim() || null,
        filter_categories: selectedCategories.length > 0 ? selectedCategories : null
    };
}

// Load categories from API
async function loadCategories() {
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key) {
        showAlert('Please configure S&S Activewear API credentials first', 'warning');
        return;
    }
    
    showAlert('Loading categories...', 'info');
    
    try {
        const response = await fetch('/api/categories', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
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
            showAlert('Failed to load categories: ' + result.message, 'danger');
        }
    } catch (error) {
        showAlert('Error loading categories: ' + error.message, 'danger');
    }
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
        showAlert('Please fill in all API credentials first', 'warning');
        return;
    }
    
    showAlert('Testing connections...', 'info');
    
    try {
        const response = await fetch('/api/test-connection', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        // Display results
        const resultsDiv = document.getElementById('connectionResults');
        const resultsBody = document.getElementById('connectionResultsBody');
        
        let html = '';
        result.messages.forEach(msg => {
            const isSuccess = msg.includes('successfully') || msg.includes('Connected');
            html += `
                <div class="mb-2">
                    <span class="badge ${isSuccess ? 'bg-success' : 'bg-danger'}">${msg}</span>
                </div>
            `;
        });
        
        resultsBody.innerHTML = html;
        resultsDiv.style.display = 'block';
        
        if (result.ss && result.shopify) {
            showAlert('Both connections successful!', 'success');
        } else {
            showAlert('One or more connections failed', 'warning');
        }
    } catch (error) {
        showAlert('Error testing connections: ' + error.message, 'danger');
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
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            showAlert('Synchronization started!', 'success');
            document.getElementById('startBtn').disabled = true;
            document.getElementById('stopBtn').disabled = false;
            document.getElementById('progressSection').style.display = 'block';
            document.getElementById('statsSection').style.display = 'block';
        } else {
            showAlert('Failed to start sync: ' + result.message, 'danger');
        }
    } catch (error) {
        showAlert('Error starting sync: ' + error.message, 'danger');
    }
}

// Stop sync
async function stopSync() {
    try {
        const response = await fetch('/api/sync/stop', {
            method: 'POST'
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            showAlert('Synchronization stopped', 'warning');
            document.getElementById('startBtn').disabled = false;
            document.getElementById('stopBtn').disabled = true;
        }
    } catch (error) {
        showAlert('Error stopping sync: ' + error.message, 'danger');
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
        const response = await fetch('/api/preview', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            displayPreview(result.products);
            showAlert(`Loaded ${result.count} products for preview`, 'success');
        } else {
            showAlert('Failed to load preview: ' + result.message, 'danger');
        }
    } catch (error) {
        showAlert('Error loading preview: ' + error.message, 'danger');
    }
}

// Display preview table
function displayPreview(products) {
    const tbody = document.getElementById('previewTableBody');
    const previewDiv = document.getElementById('previewResults');
    
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
    
    previewDiv.style.display = 'block';
}

// Poll sync status
let statusPollInterval = null;

function startStatusPolling() {
    statusPollInterval = setInterval(async () => {
        try {
            const response = await fetch('/api/sync/status');
            const status = await response.json();
            
            updateSyncStatus(status);
        } catch (error) {
            console.error('Error polling status:', error);
        }
    }, 2000); // Poll every 2 seconds
}

function updateSyncStatus(status) {
    if (status.status === 'idle') {
        return;
    }
    
    // Update progress
    document.getElementById('progressBar').style.width = status.progress + '%';
    document.getElementById('progressBar').textContent = status.progress + '%';
    document.getElementById('progressPercent').textContent = status.progress + '%';
    document.getElementById('progressText').textContent = status.message || 'Processing...';
    
    // Update stats
    if (status.stats) {
        document.getElementById('statTotal').textContent = status.stats.total || 0;
        document.getElementById('statCreated').textContent = status.stats.created || 0;
        document.getElementById('statUpdated').textContent = status.stats.updated || 0;
        document.getElementById('statErrors').textContent = status.stats.errors || 0;
    }
    
    // Update status message
    document.getElementById('statusMessage').textContent = status.message || '';
    document.getElementById('statusAlert').style.display = 'block';
    
    // Update buttons
    if (status.status === 'completed' || status.status === 'error') {
        document.getElementById('startBtn').disabled = false;
        document.getElementById('stopBtn').disabled = true;
    }
    
    // Display errors
    if (status.errors && status.errors.length > 0) {
        displayErrors(status.errors);
    }
}

function displayErrors(errors) {
    const tbody = document.getElementById('errorLogBody');
    const errorDiv = document.getElementById('errorLog');
    
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
    
    errorDiv.style.display = 'block';
}

// Test endpoints
async function testEndpoints() {
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key) {
        showAlert('Please configure S&S Activewear API credentials first', 'warning');
        return;
    }
    
    showAlert('Testing endpoint access...', 'info');
    
    try {
        const response = await fetch('/api/test-endpoints', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            displayEndpointResults(result.results);
            showAlert('Endpoint test completed', 'success');
        } else {
            showAlert('Failed to test endpoints: ' + result.message, 'danger');
        }
    } catch (error) {
        showAlert('Error testing endpoints: ' + error.message, 'danger');
    }
}

// Display endpoint test results
function displayEndpointResults(results) {
    const tbody = document.getElementById('endpointResultsBody');
    const endpointDiv = document.getElementById('endpointResults');
    const warningDiv = document.getElementById('regionalWarning');
    
    tbody.innerHTML = '';
    
    const endpoints = [
        { key: 'categories', name: 'Categories' },
        { key: 'brands', name: 'Brands' },
        { key: 'styles', name: 'Styles' },
        { key: 'products', name: 'Products' }
    ];
    
    let has403Error = false;
    
    endpoints.forEach(endpoint => {
        const row = document.createElement('tr');
        const isSuccess = results[endpoint.key];
        const error = results.errors[endpoint.key] || '';
        
        if (error.includes('403') || error.includes('Forbidden')) {
            has403Error = true;
        }
        
        row.innerHTML = `
            <td><strong>${endpoint.name}</strong></td>
            <td>
                ${isSuccess 
                    ? '<span class="badge bg-success">✓ Accessible</span>' 
                    : '<span class="badge bg-danger">✗ Failed</span>'}
            </td>
            <td><small>${error || 'No error'}</small></td>
        `;
        tbody.appendChild(row);
    });
    
    endpointDiv.style.display = 'block';
    
    // Show regional warning if 403 errors detected
    if (has403Error) {
        warningDiv.style.display = 'block';
    } else {
        warningDiv.style.display = 'none';
    }
}

// Show alert
function showAlert(message, type) {
    const alertDiv = document.getElementById('statusAlert');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.querySelector('#statusMessage').textContent = message;
    alertDiv.style.display = 'block';
    
    setTimeout(() => {
        if (type !== 'info') {
            alertDiv.style.display = 'none';
        }
    }, 5000);
}

