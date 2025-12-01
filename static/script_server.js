// Global variables
let statusPollInterval = null;
let currentProductPollInterval = null;

// Make showSection global - must be defined before DOMContentLoaded
window.showSection = function(sectionName) {
    console.log('showSection called with:', sectionName);
    
    // Hide all sections
    const allSections = document.querySelectorAll('.content-section');
    console.log('Found sections:', allSections.length);
    allSections.forEach(section => {
        section.classList.remove('active');
    });
    
    // Show selected section
    const sectionId = `section-${sectionName}`;
    const section = document.getElementById(sectionId);
    console.log('Looking for section:', sectionId, 'Found:', !!section);
    
    if (section) {
        section.classList.add('active');
        console.log('Section activated:', sectionId);
    } else {
        console.error(`Section not found: ${sectionId}`);
        alert(`Section not found: ${sectionId}`);
    }
    
    // Update menu
    document.querySelectorAll('.sidebar-menu a').forEach(link => {
        link.classList.remove('active');
    });
    const menuItem = document.getElementById(`menu-${sectionName}`);
    if (menuItem) {
        menuItem.classList.add('active');
        console.log('Menu item activated:', sectionName);
    }
    
    // Load section-specific data
    if (sectionName === 'auto-sync') {
        loadAutoSyncStatus();
    } else if (sectionName === 'dashboard') {
        updateDashboard();
    }
};

// Load on page ready
document.addEventListener('DOMContentLoaded', function() {
    loadConfiguration();
    startStatusPolling();
    loadAutoSyncStatus();
    showSection('dashboard');
    
    // Setup form event listener
    const configForm = document.getElementById('configForm');
    if (configForm) {
        configForm.addEventListener('submit', handleConfigSubmit);
    }
    
    // Setup menu click handlers as backup (onclick already in HTML)
    document.querySelectorAll('.sidebar-menu a').forEach(link => {
        link.addEventListener('click', function(e) {
            const onclickAttr = this.getAttribute('onclick');
            if (onclickAttr && onclickAttr.includes('showSection')) {
                // Extract section name from onclick
                const match = onclickAttr.match(/showSection\('(.+?)'\)/);
                if (match && match[1]) {
                    const sectionName = match[1];
                    e.preventDefault();
                    e.stopPropagation();
                    if (window.showSection) {
                        window.showSection(sectionName);
                    }
                }
            }
        });
    });
    
    console.log('Menu handlers setup complete. showSection available:', typeof window.showSection);
});

// Handle config form submit
async function handleConfigSubmit(e) {
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
        showAlert(result.status === 'success' ? 'Configuration saved successfully!' : 'Failed to save configuration', 
                  result.status === 'success' ? 'success' : 'danger');
    } catch (error) {
        showAlert('Error saving configuration: ' + error.message, 'danger');
        console.error('Config save error:', error);
    }
}

// Update dashboard
function updateDashboard() {
    // Update dashboard stats if available
    fetch('/api/sync/status')
        .then(response => response.json())
        .then(status => {
            if (status.stats) {
                updateElement('stat-total', status.stats.total || 0);
                updateElement('stat-created', status.stats.created || 0);
                updateElement('stat-updated', status.stats.updated || 0);
                updateElement('stat-errors', status.stats.errors || 0);
            }
            
            const dashboardStatus = document.getElementById('dashboard-status');
            if (dashboardStatus) {
                if (status.status === 'idle') {
                    dashboardStatus.innerHTML = '<p class="text-muted">Henüz aktarım yapılmadı</p>';
                } else {
                    dashboardStatus.innerHTML = `
                        <p><strong>Durum:</strong> ${status.status}</p>
                        <p><strong>Mesaj:</strong> ${status.message || 'N/A'}</p>
                        <p><strong>İlerleme:</strong> ${status.progress || 0}%</p>
                    `;
                }
            }
        })
        .catch(err => console.error('Dashboard update error:', err));
}

// Load configuration
// Load configuration - ENHANCED VERSION
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
            }
            
            // Load filter values if elements exist
            const filterPartNumber = document.getElementById('filterPartNumber');
            const filterWarehouses = document.getElementById('filterWarehouses');
            const filterSku = document.getElementById('filterSku');
            if (filterPartNumber) filterPartNumber.value = data.sync_options.filter_partnumber || '';
            if (filterWarehouses) filterWarehouses.value = data.sync_options.filter_warehouses || '';
            if (filterSku) filterSku.value = data.sync_options.filter_sku || '';
            
            // Load selected filters from saved options
            if (data.sync_options.filter_categories) {
                selectedCategories = Array.isArray(data.sync_options.filter_categories) 
                    ? data.sync_options.filter_categories 
                    : [data.sync_options.filter_categories];
                // Load categories first, then restore checkboxes
                if (selectedCategories.length > 0) {
                    await loadCategories();
                    // Wait a bit for categories to load, then restore checkboxes
                    setTimeout(() => {
                        selectedCategories.forEach(catId => {
                            const checkbox = document.querySelector(\input.category-checkbox[value=" \\]\);
 if (checkbox) checkbox.checked = true;
 });
 // Update select all checkbox
 const selectAllCats = document.getElementById('selectAllCategories');
 if (selectAllCats) {
 const allChecked = document.querySelectorAll('.category-checkbox').length === 
 document.querySelectorAll('.category-checkbox:checked').length;
 selectAllCats.checked = allChecked;
 }
 // Enable next button if categories selected
 const step1NextBtn = document.getElementById('step1NextBtn');
 if (step1NextBtn) step1NextBtn.disabled = selectedCategories.length === 0;
 }, 1000);
 }
 }
 
 if (data.sync_options.filter_styles && selectedCategories.length > 0) {
 selectedStyles = Array.isArray(data.sync_options.filter_styles) 
 ? data.sync_options.filter_styles 
 : [data.sync_options.filter_styles];
 // Load styles first, then restore checkboxes
 if (selectedStyles.length > 0) {
 setTimeout(async () => {
 await loadStyles();
 // Wait for styles to load, then restore checkboxes
 setTimeout(() => {
 selectedStyles.forEach(styleId => {
 const checkbox = document.querySelector(\input.style-checkbox[value=\\\]\);
 if (checkbox) checkbox.checked = true;
 });
 // Update select all checkbox
 const selectAllStyles = document.getElementById('selectAllStyles');
 if (selectAllStyles) {
 const allChecked = document.querySelectorAll('.style-checkbox').length === 
 document.querySelectorAll('.style-checkbox:checked').length;
 selectAllStyles.checked = allChecked;
 }
 // Enable next button if styles selected
 const step2NextBtn = document.getElementById('step2NextBtn');
 if (step2NextBtn) step2NextBtn.disabled = selectedStyles.length === 0;
 }, 2000);
 }, 1500);
 }
 }
 
 if (data.sync_options.filter_brands && selectedStyles.length > 0) {
 selectedBrands = Array.isArray(data.sync_options.filter_brands) 
 ? data.sync_options.filter_brands 
 : [data.sync_options.filter_brands];
 // Load brands first, then restore checkboxes
 if (selectedBrands.length > 0) {
 setTimeout(async () => {
 await loadBrands();
 // Wait for brands to load, then restore checkboxes
 setTimeout(() => {
 selectedBrands.forEach(brandName => {
 const checkbox = document.querySelector(\input.brand-checkbox[value=\\\]\);
 if (checkbox) checkbox.checked = true;
 });
 // Update select all checkbox
 const selectAllBrands = document.getElementById('selectAllBrands');
 if (selectAllBrands) {
 const allChecked = document.querySelectorAll('.brand-checkbox').length === 
 document.querySelectorAll('.brand-checkbox:checked').length;
 selectAllBrands.checked = allChecked;
 }
 // Enable next button if brands selected
 const step3NextBtn = document.getElementById('step3NextBtn');
 if (step3NextBtn) step3NextBtn.disabled = selectedBrands.length === 0;
 }, 2000);
 }, 4000);
 }
 }
 
 // Show filters summary if filters are selected
 if ((selectedCategories && selectedCategories.length > 0) || 
 (selectedStyles && selectedStyles.length > 0) || 
 (selectedBrands && selectedBrands.length > 0)) {
 setTimeout(() => {
 const summaryDiv = document.getElementById('filtersSummaryContent');
 if (summaryDiv) {
 summaryDiv.innerHTML = \
 <p><strong>SeÃ§ilen Kategoriler:</strong> \ adet</p>
 <p><strong>SeÃ§ilen Stiller:</strong> \ adet</p>
 <p><strong>SeÃ§ilen Markalar:</strong> \ adet</p>
 <p><strong>Part Number:</strong> \</p>
 <p><strong>Depo:</strong> \</p>
 <p><strong>SKU:</strong> \</p>
 \;
 document.getElementById('filtersSummary').style.display = 'block';
 }
 }, 6000);
 }
 
 // Load auto sync options
 if (document.getElementById('autoSyncUpdateInventory')) {
 document.getElementById('autoSyncUpdateInventory').checked = data.sync_options.update_inventory !== false;
 }
 if (document.getElementById('autoSyncUpdatePrices')) {
 document.getElementById('autoSyncUpdatePrices').checked = data.sync_options.update_prices !== false;
 }
 if (document.getElementById('autoSyncUpdateImages')) {
 document.getElementById('autoSyncUpdateImages').checked = data.sync_options.update_images !== false;
 }
 if (document.getElementById('autoSyncCreateNew')) {
 document.getElementById('autoSyncCreateNew').checked = data.sync_options.create_new !== false;
 }
 if (document.getElementById('autoSyncUpdateExisting')) {
 document.getElementById('autoSyncUpdateExisting').checked = data.sync_options.update_existing !== false;
 }
 if (document.getElementById('autoSyncUpdateCollections')) {
 document.getElementById('autoSyncUpdateCollections').checked = data.sync_options.sync_collections !== false;
 }
 }
 } catch (error) {
 console.error('Failed to load configuration:', error);
 }
}
// Config form submit is now handled by handleConfigSubmit function above

// Get sync options
function getSyncOptions() {
    return {
        sync_all_products: document.getElementById('syncAllProducts')?.checked ?? true,
        create_new: document.getElementById('createNew')?.checked ?? true,
        update_existing: document.getElementById('updateExisting')?.checked ?? true,
        sync_collections: document.getElementById('syncCollections')?.checked ?? true,
        create_collections: document.getElementById('createCollections')?.checked ?? true,
        create_brand_collections: document.getElementById('createBrandCollections')?.checked ?? true,
        sync_tags: document.getElementById('syncTags')?.checked ?? true,
        set_active: document.getElementById('setActive')?.checked ?? true,
        filter_categories: selectedCategories.length > 0 ? selectedCategories : null,
        filter_styles: selectedStyles.length > 0 ? selectedStyles : null,
        filter_brands: selectedBrands.length > 0 ? selectedBrands : null,
        filter_partnumber: document.getElementById('filterPartNumber')?.value.trim() || null,
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

// Multi-step filter state
let selectedCategories = [];
let selectedStyles = [];
let selectedBrands = [];

// Step navigation
function goToStep1() {
    document.getElementById('step1-tab').click();
}

function goToStep2() {
    const selected = getSelectedCategories();
    if (selected.length === 0) {
        showAlert('Lütfen en az bir kategori seçin', 'warning');
        return;
    }
    selectedCategories = selected;
    document.getElementById('step2-tab').disabled = false;
    document.getElementById('step2-tab').click();
    // Automatically load styles when moving to step 2
    setTimeout(() => {
        loadStyles();
    }, 300);
}

function goToStep3() {
    const selected = getSelectedStyles();
    if (selected.length === 0) {
        showAlert('Lütfen en az bir stil seçin', 'warning');
        return;
    }
    selectedStyles = selected;
    document.getElementById('step3-tab').disabled = false;
    document.getElementById('step3-tab').click();
    loadBrands();
}

function goToStep4() {
    const selected = getSelectedBrands();
    if (selected.length === 0) {
        showAlert('Lütfen en az bir marka seçin', 'warning');
        return;
    }
    selectedBrands = selected;
    document.getElementById('step4-tab').disabled = false;
    document.getElementById('step4-tab').click();
}

// Load categories - automatically loads on page load if API credentials exist
async function loadCategories() {
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key) {
        showAlert('Lütfen önce API bilgilerini yapılandırın', 'warning');
        return;
    }
    
    const loadBtn = document.querySelector('button[onclick="loadCategories()"]');
    if (loadBtn) {
        loadBtn.disabled = true;
        loadBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Yükleniyor...';
    }
    
    showAlert('Kategoriler yükleniyor...', 'info');
    
    try {
        const response = await fetch('/api/categories', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            const categoriesList = document.getElementById('categoriesList');
            categoriesList.innerHTML = '';
            
            result.categories.forEach(category => {
                const div = document.createElement('div');
                div.className = 'form-check';
                div.innerHTML = `
                    <input class="form-check-input category-checkbox" type="checkbox" 
                           value="${category.categoryID}" id="cat-${category.categoryID}"
                           onchange="updateCategorySelection()">
                    <label class="form-check-label" for="cat-${category.categoryID}">
                        ${category.name} <small class="text-muted">(ID: ${category.categoryID})</small>
                    </label>
                `;
                categoriesList.appendChild(div);
            });
            
            document.getElementById('step1NextBtn').disabled = false;
            showAlert(`${result.categories.length} kategori yüklendi`, 'success');
        } else {
            showAlert('Başarısız: ' + result.message, 'danger');
        }
    } catch (error) {
        showAlert('Hata: ' + error.message, 'danger');
    } finally {
        if (loadBtn) {
            loadBtn.disabled = false;
            loadBtn.innerHTML = '<i class="fas fa-sync"></i> Kategorileri Yükle';
        }
    }
}

// Get selected categories
function getSelectedCategories() {
    const checkboxes = document.querySelectorAll('.category-checkbox:checked');
    return Array.from(checkboxes).map(cb => cb.value);
}

// Update category selection
function updateCategorySelection() {
    const selected = getSelectedCategories();
    document.getElementById('step1NextBtn').disabled = selected.length === 0;
}

// Toggle all categories
function toggleAllCategories() {
    const selectAll = document.getElementById('selectAllCategories').checked;
    document.querySelectorAll('.category-checkbox').forEach(cb => {
        cb.checked = selectAll;
    });
    updateCategorySelection();
}

// Load styles based on selected categories - organized by category
async function loadStyles() {
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value,
        category_ids: selectedCategories
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key) {
        showAlert('Lütfen önce API bilgilerini yapılandırın', 'warning');
        return;
    }
    
    if (selectedCategories.length === 0) {
        showAlert('Lütfen önce kategorileri seçin', 'warning');
        return;
    }
    
    const loadBtn = document.getElementById('loadStylesBtn');
    if (loadBtn) {
        loadBtn.disabled = true;
        loadBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Yükleniyor...';
    }
    
    showAlert('Stiller yükleniyor, lütfen bekleyin...', 'info');
    
    try {
        const response = await fetch('/api/styles', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            const stylesList = document.getElementById('stylesList');
            stylesList.innerHTML = '<div class="text-center"><i class="fas fa-spinner fa-spin"></i> Stiller işleniyor...</div>';
            
            const stylesByCategory = result.styles_by_category || {};
            const categoryMap = result.category_map || {};
            let totalStyles = 0;
            
            // Clear and rebuild
            setTimeout(() => {
                stylesList.innerHTML = '';
                
                if (Object.keys(stylesByCategory).length > 0) {
                    // Display styles organized by category
                    selectedCategories.forEach(catId => {
                        const categoryName = categoryMap[catId] || `Kategori ${catId}`;
                        const styles = stylesByCategory[catId] || [];
                        
                        if (styles.length > 0) {
                            // Category header
                            const categoryDiv = document.createElement('div');
                            categoryDiv.className = 'mb-4';
                            categoryDiv.innerHTML = `
                                <h6 class="text-primary border-bottom pb-2 mb-3">
                                    <i class="fas fa-folder"></i> ${categoryName}
                                    <span class="badge bg-secondary ms-2">${styles.length} stil</span>
                                </h6>
                            `;
                            stylesList.appendChild(categoryDiv);
                            
                            // Styles in this category
                            const stylesContainer = document.createElement('div');
                            stylesContainer.className = 'ms-3 mb-3';
                            
                            styles.forEach(style => {
                                const div = document.createElement('div');
                                div.className = 'form-check mb-2';
                                div.innerHTML = `
                                    <input class="form-check-input style-checkbox" type="checkbox" 
                                           value="${style.styleID}" id="style-${style.styleID}"
                                           data-partnumber="${style.partNumber || ''}"
                                           data-category="${catId}"
                                           onchange="updateStyleSelection()">
                                    <label class="form-check-label" for="style-${style.styleID}">
                                        <strong>${style.brandName || ''} ${style.styleName || ''}</strong>
                                        <small class="text-muted">(${style.partNumber || ''})</small>
                                    </label>
                                `;
                                stylesContainer.appendChild(div);
                                totalStyles++;
                            });
                            
                            categoryDiv.appendChild(stylesContainer);
                        }
                    });
                    
                    if (totalStyles > 0) {
                        document.getElementById('step2NextBtn').disabled = false;
                        document.getElementById('loadStylesBtn').style.display = 'inline-block';
                        showAlert(`${totalStyles} stil ${Object.keys(stylesByCategory).length} kategoride yüklendi`, 'success');
                    } else {
                        stylesList.innerHTML = '<p class="text-muted text-center">Bu kategoriler için stil bulunamadı</p>';
                        showAlert('Bu kategoriler için stil bulunamadı', 'warning');
                    }
                } else {
                    stylesList.innerHTML = '<p class="text-muted text-center">Bu kategoriler için stil bulunamadı</p>';
                    showAlert('Bu kategoriler için stil bulunamadı', 'warning');
                }
            }, 100);
        } else {
            showAlert('Başarısız: ' + (result.message || 'Bilinmeyen hata'), 'danger');
            console.error('Styles API Error:', result);
            document.getElementById('loadStylesBtn').style.display = 'inline-block';
        }
    } catch (error) {
        showAlert('Hata: ' + error.message, 'danger');
        console.error('Styles Load Error:', error);
    } finally {
        if (loadBtn) {
            loadBtn.disabled = false;
            loadBtn.innerHTML = '<i class="fas fa-sync"></i> Stilleri Yükle';
        }
    }
}

// Get selected styles
function getSelectedStyles() {
    const checkboxes = document.querySelectorAll('.style-checkbox:checked');
    return Array.from(checkboxes).map(cb => cb.value);
}

// Update style selection
function updateStyleSelection() {
    const selected = getSelectedStyles();
    document.getElementById('step2NextBtn').disabled = selected.length === 0;
}

// Toggle all styles
function toggleAllStyles() {
    const selectAll = document.getElementById('selectAllStyles').checked;
    document.querySelectorAll('.style-checkbox').forEach(cb => {
        cb.checked = selectAll;
    });
    updateStyleSelection();
}

// Load brands based on selected styles - organized by style
async function loadBrands() {
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value,
        style_ids: selectedStyles
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key) {
        showAlert('Lütfen önce API bilgilerini yapılandırın', 'warning');
        return;
    }
    
    if (selectedStyles.length === 0) {
        showAlert('Lütfen önce stilleri seçin', 'warning');
        return;
    }
    
    const loadBtn = document.getElementById('loadBrandsBtn');
    if (loadBtn) {
        loadBtn.disabled = true;
        loadBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Yükleniyor...';
    }
    
    showAlert('Markalar yükleniyor...', 'info');
    
    try {
        const response = await fetch('/api/brands', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            const brandsList = document.getElementById('brandsList');
            brandsList.innerHTML = '';
            
            const brandsByStyle = result.brands_by_style || {};
            const styleMap = result.style_map || {};
            const allBrands = result.all_brands || [];
            let totalBrands = 0;
            const uniqueBrands = new Set();
            
            if (Object.keys(brandsByStyle).length > 0) {
                // Display brands organized by brand name (each brand shows its styles)
                Object.keys(brandsByStyle).sort().forEach(brandName => {
                    const styles = brandsByStyle[brandName];
                    uniqueBrands.add(brandName);
                    
                    // Brand header
                    const brandDiv = document.createElement('div');
                    brandDiv.className = 'mb-4';
                    brandDiv.innerHTML = `
                        <h6 class="text-success border-bottom pb-2 mb-3">
                            <i class="fas fa-tag"></i> ${brandName}
                            <span class="badge bg-secondary ms-2">${styles.length} stil</span>
                        </h6>
                    `;
                    brandsList.appendChild(brandDiv);
                    
                    // Styles for this brand
                    const stylesContainer = document.createElement('div');
                    stylesContainer.className = 'ms-3 mb-3';
                    
                    styles.forEach(styleInfo => {
                        const div = document.createElement('div');
                        div.className = 'form-check mb-2';
                        div.innerHTML = `
                            <input class="form-check-input brand-checkbox" type="checkbox" 
                                   value="${brandName}" id="brand-${brandName}-${styleInfo.styleID}"
                                   data-name="${brandName}"
                                   data-styleid="${styleInfo.styleID}"
                                   onchange="updateBrandSelection()">
                            <label class="form-check-label" for="brand-${brandName}-${styleInfo.styleID}">
                                ${styleInfo.styleName || ''} <small class="text-muted">(${styleInfo.partNumber || ''})</small>
                            </label>
                        `;
                        stylesContainer.appendChild(div);
                        totalBrands++;
                    });
                    
                    brandDiv.appendChild(stylesContainer);
                });
                
                if (uniqueBrands.size > 0) {
                    document.getElementById('step3NextBtn').disabled = false;
                    showAlert(`${uniqueBrands.size} marka, ${totalBrands} stil yüklendi`, 'success');
                } else {
                    brandsList.innerHTML = '<p class="text-muted text-center">Seçilen stiller için marka bulunamadı</p>';
                    showAlert('Seçilen stiller için marka bulunamadı', 'warning');
                }
            } else {
                brandsList.innerHTML = '<p class="text-muted text-center">Seçilen stiller için marka bulunamadı</p>';
                showAlert('Seçilen stiller için marka bulunamadı', 'warning');
            }
        } else {
            showAlert('Başarısız: ' + (result.message || 'Bilinmeyen hata'), 'danger');
            console.error('Brands API Error:', result);
        }
    } catch (error) {
        showAlert('Hata: ' + error.message, 'danger');
        console.error('Brands Load Error:', error);
    } finally {
        if (loadBtn) {
            loadBtn.disabled = false;
            loadBtn.innerHTML = '<i class="fas fa-sync"></i> Markaları Yükle';
        }
    }
}

// Get selected brands
function getSelectedBrands() {
    const checkboxes = document.querySelectorAll('.brand-checkbox:checked');
    return Array.from(checkboxes).map(cb => cb.value);
}

// Update brand selection
function updateBrandSelection() {
    const selected = getSelectedBrands();
    document.getElementById('step3NextBtn').disabled = selected.length === 0;
}

// Toggle all brands
function toggleAllBrands() {
    const selectAll = document.getElementById('selectAllBrands').checked;
    document.querySelectorAll('.brand-checkbox').forEach(cb => {
        cb.checked = selectAll;
    });
    updateBrandSelection();
}

// Save filters
function saveFilters() {
    selectedBrands = getSelectedBrands();
    
    // Update filter summary
    const summaryDiv = document.getElementById('filtersSummaryContent');
    summaryDiv.innerHTML = `
        <p><strong>Seçilen Kategoriler:</strong> ${selectedCategories.length} adet</p>
        <p><strong>Seçilen Stiller:</strong> ${selectedStyles.length} adet</p>
        <p><strong>Seçilen Markalar:</strong> ${selectedBrands.length} adet</p>
        <p><strong>Part Number:</strong> ${document.getElementById('filterPartNumber').value || 'Yok'}</p>
        <p><strong>Depo:</strong> ${document.getElementById('filterWarehouses').value || 'Yok'}</p>
        <p><strong>SKU:</strong> ${document.getElementById('filterSku').value || 'Yok'}</p>
    `;
    
    document.getElementById('filtersSummary').style.display = 'block';
    showAlert('Filtreler kaydedildi! Şimdi "Aktarım Ayarlarını Kaydet" butonuna tıklayın.', 'success');
}

// Save transfer settings
async function saveTransferSettings() {
    const btn = document.getElementById('saveTransferSettingsBtn');
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Kaydediliyor...';
    }
    
    try {
        const syncOptions = getSyncOptions();
        const configData = {
            ss_account_number: document.getElementById('ssAccountNumber').value,
            ss_api_key: document.getElementById('ssApiKey').value,
            shopify_domain: document.getElementById('shopifyDomain').value,
            shopify_token: document.getElementById('shopifyToken').value,
            sync_options: syncOptions
        };
        
        const response = await fetch('/api/config', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            showAlert('Aktarım ayarları başarıyla kaydedildi! Artık aktarım yapabilirsiniz.', 'success');
            // Scroll to sync section
            setTimeout(() => {
                showSection('sync-active');
            }, 1000);
        } else {
            showAlert('Hata: ' + (result.message || 'Ayarlar kaydedilemedi'), 'danger');
        }
    } catch (error) {
        showAlert('Hata: ' + error.message, 'danger');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-save"></i> Aktarım Ayarlarını Kaydet';
        }
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
    // Find the active section
    const activeSection = document.querySelector('.content-section.active');
    if (!activeSection) {
        alert(message);
        return;
    }
    
    // Try to find statusAlertContainer or create alert
    let container = activeSection.querySelector('#statusAlertContainer');
    if (!container) {
        // Create container in the first card
        const firstCard = activeSection.querySelector('.card');
        if (firstCard) {
            container = document.createElement('div');
            container.id = 'statusAlertContainer';
            const cardBody = firstCard.querySelector('.card-body');
            if (cardBody) {
                cardBody.insertBefore(container, cardBody.firstChild);
            }
        }
    }
    
    if (container) {
        // Remove existing alerts
        container.innerHTML = '';
        
        // Create new alert
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
        alertDiv.innerHTML = `
            <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'danger' ? 'exclamation-circle' : type === 'warning' ? 'exclamation-triangle' : 'info-circle'}"></i>
            <span>${message}</span>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        container.appendChild(alertDiv);
        
        // Auto-hide after 5 seconds (except info)
        if (type !== 'info') {
            setTimeout(() => {
                if (alertDiv && alertDiv.classList) {
                    alertDiv.classList.remove('show');
                    setTimeout(() => {
                        if (alertDiv.parentNode) {
                            alertDiv.remove();
                        }
                    }, 150);
                }
            }, 5000);
        }
    } else {
        // Fallback
        alert(message);
    }
}

