// Global variables
let statusPollInterval = null;
let currentProductPollInterval = null;
let selectedCategories = [];
let selectedStyles = [];
let selectedBrands = [];

// Make showSection global - REPLACE placeholder from HTML head
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
        updateAutoSyncFiltersDisplay();
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
    
    // Setup menu click handlers using data-section attribute (NO onclick!)
    document.querySelectorAll('.sidebar-menu a[data-section]').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            const sectionName = this.getAttribute('data-section');
            if (sectionName && window.showSection) {
                window.showSection(sectionName);
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
                            const checkbox = document.querySelector(`input.category-checkbox[value="${catId}"]`);
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
            
            if (data.sync_options.filter_styles && selectedCategories && selectedCategories.length > 0) {
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
                                const checkbox = document.querySelector(`input.style-checkbox[value="${styleId}"]`);
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
            
            if (data.sync_options.filter_brands && selectedStyles && selectedStyles.length > 0) {
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
                                const checkbox = document.querySelector(`input.brand-checkbox[value="${brandName}"]`);
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
                        const catCount = selectedCategories ? selectedCategories.length : 0;
                        const styleCount = selectedStyles ? selectedStyles.length : 0;
                        const brandCount = selectedBrands ? selectedBrands.length : 0;
                        const estimatedProducts = styleCount * 50; // Average 50 variants per style
                        
                        summaryDiv.innerHTML = `
                            <p><strong>Seçilen Kategoriler:</strong> ${catCount} adet</p>
                            <p><strong>Seçilen Stiller:</strong> ${styleCount} adet</p>
                            <p><strong>Seçilen Markalar:</strong> ${brandCount} adet</p>
                            <p><strong>Tahmini Toplam Ürün Sayısı:</strong> <span class="badge bg-primary">~${estimatedProducts.toLocaleString()} adet</span></p>
                            <p><strong>Part Number:</strong> ${data.sync_options.filter_partnumber || 'Yok'}</p>
                            <p><strong>Depo:</strong> ${data.sync_options.filter_warehouses || 'Yok'}</p>
                            <p><strong>SKU:</strong> ${data.sync_options.filter_sku || 'Yok'}</p>
                        `;
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
// Get sync options - CRITICAL: Must use selectedCategories, selectedStyles, selectedBrands
window.getSyncOptions = function getSyncOptions() {
    const options = {
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
        filter_warehouses: window.getSelectedWarehouses ? window.getSelectedWarehouses() : [],
        filter_sku: document.getElementById('filterSku')?.value.trim() || null,
        price_field: document.getElementById('priceField')?.value || 'customerPrice',
        inventory_management: document.getElementById('inventoryManagement')?.value || 'shopify',
        image_size: document.getElementById('imageSize')?.value || '_fl',
        update_inventory: document.getElementById('updateInventory')?.checked ?? true,
        update_prices: document.getElementById('updatePrices')?.checked ?? true,
        update_images: document.getElementById('updateImages')?.checked ?? true
    };
    
    // Debug logging
    console.log('Sync Options:', {
        categories: options.filter_categories,
        styles: options.filter_styles,
        brands: options.filter_brands,
        selectedCategories: selectedCategories,
        selectedStyles: selectedStyles,
        selectedBrands: selectedBrands
    });
    
    return options;
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
    // Get sync options - use saved ones if available
    const syncOptions = getSyncOptions();
    
    // Debug: Log what we're sending
    console.log('Starting sync with options:', syncOptions);
    console.log('Selected categories:', selectedCategories);
    console.log('Selected styles:', selectedStyles);
    console.log('Selected brands:', selectedBrands);
    
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value,
        shopify_domain: document.getElementById('shopifyDomain').value,
        shopify_token: document.getElementById('shopifyToken').value,
        sync_options: syncOptions
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key || 
        !configData.shopify_domain || !configData.shopify_token) {
        showAlert('Lütfen önce API bilgilerini yapılandırın', 'warning');
        return;
    }
    
    // Check if filters are selected
    if (!syncOptions.filter_categories && !syncOptions.filter_styles && !syncOptions.filter_brands && 
        !syncOptions.filter_partnumber && !syncOptions.filter_sku) {
        const confirmNoFilters = confirm(
            'Hiçbir filtre seçilmedi. Tüm ürünler aktarılacak. Devam etmek istiyor musunuz?'
        );
        if (!confirmNoFilters) {
            return;
        }
    }
    
    try {
        const response = await fetch('/api/sync/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(configData)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            showAlert('Aktarım başlatıldı!', 'success');
            document.getElementById('startBtn').disabled = true;
            document.getElementById('stopBtn').disabled = false;
            document.getElementById('progressSection').style.display = 'block';
            document.getElementById('currentProductCard').style.display = 'block';
            document.getElementById('transferConsoleCard').style.display = 'block';
            document.getElementById('createdProductsCard').style.display = 'none'; // Hide until sync completes
            clearConsole();
            startCurrentProductPolling();
            startStatusPolling();
            showSection('sync-active');
        } else {
            showAlert('Başlatılamadı: ' + result.message, 'danger');
        }
    } catch (error) {
        showAlert('Hata: ' + error.message, 'danger');
        console.error('Sync start error:', error);
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

// Multi-step filter state (variables already declared at top)

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

// Filter categories by search - GLOBAL FUNCTION
window.filterCategories = function filterCategories() {
    const searchTerm = document.getElementById('categorySearch')?.value?.toLowerCase() || '';
    const checkboxes = document.querySelectorAll('.category-checkbox');
    checkboxes.forEach(cb => {
        const label = cb.closest('.form-check');
        if (label) {
            const text = label.textContent.toLowerCase();
            if (text.includes(searchTerm)) {
                label.style.display = '';
            } else {
                label.style.display = 'none';
            }
        }
    });
};

// Filter styles by search - GLOBAL FUNCTION
window.filterStyles = function filterStyles() {
    const searchTerm = document.getElementById('styleSearch').value.toLowerCase();
    const styleItems = document.querySelectorAll('.style-checkbox, .form-check');
    styleItems.forEach(item => {
        const text = item.textContent.toLowerCase();
        const parent = item.closest('.form-check, .mb-4');
        if (parent && item.classList.contains('style-checkbox')) {
            if (text.includes(searchTerm)) {
                parent.style.display = '';
            } else {
                // Check if it's a category header
                if (!parent.querySelector('.style-checkbox')) {
                    // It's a category header, check if any children match
                    const hasVisibleChildren = Array.from(parent.querySelectorAll('.style-checkbox')).some(cb => {
                        const cbText = cb.closest('.form-check')?.textContent.toLowerCase() || '';
                        return cbText.includes(searchTerm);
                    });
                    parent.style.display = hasVisibleChildren ? '' : 'none';
                } else {
                    parent.style.display = text.includes(searchTerm) ? '' : 'none';
                }
            }
        } else if (item.classList.contains('style-checkbox')) {
            const formCheck = item.closest('.form-check');
            if (formCheck) {
                formCheck.style.display = text.includes(searchTerm) ? '' : 'none';
            }
        }
    });
};

// Filter brands by search - GLOBAL FUNCTION
window.filterBrands = function filterBrands() {
    const searchTerm = document.getElementById('brandSearch').value.toLowerCase();
    const brandItems = document.querySelectorAll('.brand-checkbox, .form-check');
    brandItems.forEach(item => {
        const text = item.textContent.toLowerCase();
        const parent = item.closest('.form-check, .mb-4');
        if (parent && item.classList.contains('brand-checkbox')) {
            if (text.includes(searchTerm)) {
                parent.style.display = '';
            } else {
                // Check if it's a brand header
                if (!parent.querySelector('.brand-checkbox')) {
                    // It's a brand header, check if any children match
                    const hasVisibleChildren = Array.from(parent.querySelectorAll('.brand-checkbox')).some(cb => {
                        const cbText = cb.closest('.form-check')?.textContent.toLowerCase() || '';
                        return cbText.includes(searchTerm);
                    });
                    parent.style.display = hasVisibleChildren ? '' : 'none';
                } else {
                    parent.style.display = text.includes(searchTerm) ? '' : 'none';
                }
            }
        } else if (item.classList.contains('brand-checkbox')) {
            const formCheck = item.closest('.form-check');
            if (formCheck) {
                formCheck.style.display = text.includes(searchTerm) ? '' : 'none';
            }
        }
    });
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
async function saveFilters() {
    selectedBrands = getSelectedBrands();
    
    // Get selected warehouses from warehouse_ui.js
    const selectedWarehouseCodes = window.getSelectedWarehouses ? window.getSelectedWarehouses() : [];
    
    // Update filter summary
    const summaryDiv = document.getElementById('filtersSummaryContent');
    summaryDiv.innerHTML = `
        <p><strong>Seçilen Lokasyonlar:</strong> ${selectedWarehouseCodes.length} adet</p>
        <p><strong>Seçilen Kategoriler:</strong> ${selectedCategories.length} adet</p>
        <p><strong>Seçilen Stiller:</strong> ${selectedStyles.length} adet</p>
        <p><strong>Seçilen Markalar:</strong> ${selectedBrands.length} adet</p>
        <p><strong>Part Number:</strong> ${document.getElementById('filterPartNumber')?.value || 'Yok'}</p>
        <p><strong>SKU:</strong> ${document.getElementById('filterSku').value || 'Yok'}</p>
    `;
    
    document.getElementById('filtersSummary').style.display = 'block';
    
    // Get actual product count from API
    try {
        const countDiv = document.getElementById('actualProductCount');
        const countValue = document.getElementById('actualCountValue');
        countDiv.style.display = 'block';
        countValue.textContent = 'Hesaplanıyor...';
        
        const syncOptions = getSyncOptions();
        const response = await fetch('/api/products/count', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                ss_account_number: document.getElementById('ssAccountNumber').value,
                ss_api_key: document.getElementById('ssApiKey').value,
                sync_options: syncOptions
            })
        });
        
        const result = await response.json();
        if (result.status === 'success') {
            countValue.textContent = `${result.count.toLocaleString()} adet`;
            countValue.className = 'badge bg-success';
        } else {
            countValue.textContent = 'Hesaplanamadı';
            countValue.className = 'badge bg-warning';
        }
    } catch (error) {
        console.error('Product count error:', error);
        const countValue = document.getElementById('actualCountValue');
        countValue.textContent = 'Hata';
        countValue.className = 'badge bg-danger';
    }
    
    // Show the save button
    const saveBtn = document.getElementById('saveTransferSettingsBtn');
    if (saveBtn) {
        saveBtn.style.display = 'block';
        saveBtn.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
    
    showAlert('Filtreler kaydedildi! Aşağıdaki "Aktarım Ayarlarını Kaydet" butonuna tıklayın.', 'success');
}

// Reset all filters - COMPLETE RESET (called from "Filtreleri Sıfırla" button) - GLOBAL FUNCTION
window.resetAllFilters = function resetAllFilters() {
    if (!confirm('Tüm filtreleri sıfırlamak istediğinizden emin misiniz? Bu işlem geri alınamaz.')) {
        return;
    }
    
    // Clear global variables
    selectedCategories = [];
    selectedStyles = [];
    selectedBrands = [];
    
    // Clear all checkboxes
    document.querySelectorAll('.category-checkbox').forEach(cb => cb.checked = false);
    document.querySelectorAll('.style-checkbox').forEach(cb => cb.checked = false);
    document.querySelectorAll('.brand-checkbox').forEach(cb => cb.checked = false);
    
    // Clear select all checkboxes
    const selectAllCats = document.getElementById('selectAllCategories');
    const selectAllStyles = document.getElementById('selectAllStyles');
    const selectAllBrands = document.getElementById('selectAllBrands');
    if (selectAllCats) selectAllCats.checked = false;
    if (selectAllStyles) selectAllStyles.checked = false;
    if (selectAllBrands) selectAllBrands.checked = false;
    
    // Clear search inputs
    const categorySearch = document.getElementById('categorySearch');
    const styleSearch = document.getElementById('styleSearch');
    const brandSearch = document.getElementById('brandSearch');
    if (categorySearch) {
        categorySearch.value = '';
        filterCategories(); // Show all items
    }
    if (styleSearch) {
        styleSearch.value = '';
        filterStyles(); // Show all items
    }
    if (brandSearch) {
        brandSearch.value = '';
        filterBrands(); // Show all items
    }
    
    // Clear other filter inputs
    const filterPartNumber = document.getElementById('filterPartNumber');
    const filterWarehouses = document.getElementById('filterWarehouses');
    const filterSku = document.getElementById('filterSku');
    if (filterPartNumber) filterPartNumber.value = '';
    if (filterWarehouses) filterWarehouses.value = '';
    if (filterSku) filterSku.value = '';
    
    // Disable next buttons
    const step1NextBtn = document.getElementById('step1NextBtn');
    const step2NextBtn = document.getElementById('step2NextBtn');
    const step3NextBtn = document.getElementById('step3NextBtn');
    if (step1NextBtn) step1NextBtn.disabled = true;
    if (step2NextBtn) step2NextBtn.disabled = true;
    if (step3NextBtn) step3NextBtn.disabled = true;
    
    // Clear summary
    const filtersSummary = document.getElementById('filtersSummary');
    const actualProductCount = document.getElementById('actualProductCount');
    if (filtersSummary) filtersSummary.style.display = 'none';
    if (actualProductCount) actualProductCount.style.display = 'none';
    
    // Reset to step 1
    const step1Tab = document.getElementById('step1-tab');
    if (step1Tab) step1Tab.click();
    
    showAlert('Tüm filtreler sıfırlandı!', 'success');
};

// Clear all filters (old function, kept for compatibility)
function clearFilters() {
    resetAllFilters();
}

// Edit filters - go back to filter steps
function editFilters() {
    showSection('sync-options');
    // Go to first step
    document.getElementById('step1-tab').click();
    showAlert('Filtreleri düzenleyebilirsiniz', 'info');
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
            // Update auto sync filters display
            updateAutoSyncFiltersDisplay();
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
    
    // Update step indicators using explicit step info
    if (status.step) {
        updateStepIndicators(status.step);
    } else {
        updateStepIndicators(status.message || '');
    }
    
    // NEW ARCHITECTURE: Update step indicators based on message
    updateStepIndicators(status.message || '');
    
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
        // Reset all steps when completed
        if (status.status === 'completed') {
            resetStepIndicators();
        }
    }
    
    // Display errors
    if (status.errors && status.errors.length > 0) {
        displayErrors(status.errors);
    }
    
    // Display logs in console
    if (status.logs && status.logs.length > 0) {
        updateConsoleLogs(status.logs);
    }
    
    // Display created products with links when sync completes
    if (status.status === 'completed' && status.created_products && status.created_products.length > 0) {
        displayCreatedProducts(status.created_products);
    }
}

// NEW ARCHITECTURE: Update step indicators
function updateStepIndicators(stepOrMessage) {
    const steps = {
        'fetch': document.getElementById('step-fetch'),
        'cache': document.getElementById('step-cache'),
        'group': document.getElementById('step-group'),
        'sync': document.getElementById('step-sync')
    };
    
    // Reset all steps
    Object.values(steps).forEach(step => {
        if (step) {
            step.classList.remove('active', 'completed');
        }
    });
    
    // Prefer explicit step id if provided
    const step = (stepOrMessage || '').toLowerCase();
    if (step === 'fetch') {
        if (steps.fetch) steps.fetch.classList.add('active');
    } else if (step === 'cache') {
        if (steps.fetch) steps.fetch.classList.add('completed');
        if (steps.cache) steps.cache.classList.add('active');
    } else if (step === 'group') {
        if (steps.fetch) steps.fetch.classList.add('completed');
        if (steps.cache) steps.cache.classList.add('completed');
        if (steps.group) steps.group.classList.add('active');
    } else if (step === 'sync') {
        if (steps.fetch) steps.fetch.classList.add('completed');
        if (steps.cache) steps.cache.classList.add('completed');
        if (steps.group) steps.group.classList.add('completed');
        if (steps.sync) steps.sync.classList.add('active');
    } else if (step === 'completed' || step === 'done') {
        // All steps completed
        Object.values(steps).forEach(step => {
            if (step) step.classList.add('completed');
        });
    } else {
        // Fallback: message parsing for older statuses
        const msg = stepOrMessage.toLowerCase();
        if (msg.includes('fetching') || msg.includes('çekiliyor') || msg.includes('fetch')) {
            if (steps.fetch) steps.fetch.classList.add('active');
        } else if (msg.includes('cached') || msg.includes('kaydediliyor') || msg.includes('database') || msg.includes('veritabanı')) {
            if (steps.fetch) steps.fetch.classList.add('completed');
            if (steps.cache) steps.cache.classList.add('active');
        } else if (msg.includes('grouping') || msg.includes('gruplanıyor') || msg.includes('group')) {
            if (steps.fetch) steps.fetch.classList.add('completed');
            if (steps.cache) steps.cache.classList.add('completed');
            if (steps.group) steps.group.classList.add('active');
        } else if (msg.includes('syncing') || msg.includes('aktarılıyor') || msg.includes('sync') || msg.includes('processing') || msg.includes('işleniyor')) {
            if (steps.fetch) steps.fetch.classList.add('completed');
            if (steps.cache) steps.cache.classList.add('completed');
            if (steps.group) steps.group.classList.add('completed');
            if (steps.sync) steps.sync.classList.add('active');
        } else if (msg.includes('completed') || msg.includes('tamamlandı')) {
            Object.values(steps).forEach(step => {
                if (step) step.classList.add('completed');
            });
        }
    }
}

// Reset step indicators
function resetStepIndicators() {
    const steps = ['step-fetch', 'step-cache', 'step-group', 'step-sync'];
    steps.forEach(stepId => {
        const step = document.getElementById(stepId);
        if (step) {
            step.classList.remove('active', 'completed');
        }
    });
}

// Current product polling
function startCurrentProductPolling() {
    if (currentProductPollInterval) clearInterval(currentProductPollInterval);
    
    currentProductPollInterval = setInterval(async () => {
        try {
            // Get status which includes current product
            const response = await fetch('/api/sync/status');
            const status = await response.json();
            
            if (status.current_product) {
                updateCurrentProductDisplay(status.current_product);
            } else if (status.status === 'running') {
                // Show fetching message if no product yet
                const productInfo = document.getElementById('currentProductInfo');
                if (productInfo) {
                    productInfo.innerHTML = `
                        <p class="text-info"><i class="fas fa-spinner fa-spin"></i> ${status.message || 'Processing...'}</p>
                    `;
                }
            }
        } catch (error) {
            console.error('Current product poll error:', error);
        }
    }, 1000);
}

// Update current product display
function updateCurrentProductDisplay(product) {
    const productInfo = document.getElementById('currentProductInfo');
    if (productInfo) {
        const title = product.title || product.sku || 'Unknown Product';
        const sku = product.sku || 'N/A';
        const index = product.index !== undefined ? product.index + 1 : 0;
        const total = product.total || 0;
        
        productInfo.innerHTML = `
            <h6>${title}</h6>
            <p class="mb-1"><strong>SKU:</strong> ${sku}</p>
            ${total > 0 ? `<p class="mb-0 text-muted"><small>Progress: ${index} / ${total}</small></p>` : ''}
        `;
    }
}

// Console log management
let lastLogCount = 0;

function updateConsoleLogs(logs) {
    if (!logs || logs.length === 0) return;
    
    const consoleOutput = document.getElementById('transferConsole');
    if (!consoleOutput) return;
    
    // Only add new logs (not already displayed)
    if (logs.length > lastLogCount) {
        const newLogs = logs.slice(lastLogCount);
        
        newLogs.forEach(log => {
            const logLine = document.createElement('div');
            logLine.className = `console-line log-${log.level || 'info'}`;
            
            const prompt = document.createElement('span');
            prompt.className = 'console-prompt';
            prompt.textContent = '$';
            
            const text = document.createElement('span');
            text.className = 'console-text';
            text.textContent = `[${log.timestamp}] ${log.message}`;
            
            logLine.appendChild(prompt);
            logLine.appendChild(text);
            consoleOutput.appendChild(logLine);
        });
        
        lastLogCount = logs.length;
        
        // Auto-scroll to bottom
        consoleOutput.scrollTop = consoleOutput.scrollHeight;
    }
}

function clearConsole() {
    const consoleOutput = document.getElementById('transferConsole');
    if (consoleOutput) {
        consoleOutput.innerHTML = '<div class="console-line"><span class="console-prompt">$</span><span class="console-text">Aktarım başlatıldı. Loglar burada görünecek...</span></div>';
        lastLogCount = 0;
    }
}

// Display created products with links
function displayCreatedProducts(products) {
    const productsCard = document.getElementById('createdProductsCard');
    const productsList = document.getElementById('createdProductsList');
    
    if (!productsCard || !productsList) return;
    
    if (!products || products.length === 0) {
        productsList.innerHTML = '<p class="text-muted">Aktarılan ürün bulunamadı.</p>';
        productsCard.style.display = 'none';
        return;
    }
    
    productsCard.style.display = 'block';
    
    let html = `<div class="alert alert-success mb-3">
        <strong>${products.length} ürün başarıyla aktarıldı!</strong>
    </div>`;
    
    html += '<div class="list-group">';
    
    products.forEach((product, index) => {
        html += `
            <div class="product-link-item">
                <div class="d-flex justify-content-between align-items-center">
                    <div>
                        <strong>${index + 1}. ${product.title || 'Ürün'}</strong>
                        <br>
                        <small class="text-muted">ID: ${product.shopify_id} | Variants: ${product.variants_count || 0}</small>
                    </div>
                    <div>
                        <a href="${product.product_url}" target="_blank" class="btn btn-sm btn-primary me-2">
                            <i class="fas fa-external-link-alt"></i> Ürün Sayfası
                        </a>
                        <a href="${product.shopify_url}" target="_blank" class="btn btn-sm btn-secondary">
                            <i class="fas fa-cog"></i> Admin
                        </a>
                    </div>
                </div>
            </div>
        `;
    });
    
    html += '</div>';
    productsList.innerHTML = html;
}

// Auto sync functions
// Update actual product count
async function updateActualProductCount() {
    const countDiv = document.getElementById('actualProductCount');
    const countValue = document.getElementById('actualCountValue');
    if (!countDiv || !countValue) return;
    
    try {
        const syncOptions = getSyncOptions();
        if (!syncOptions.filter_categories && !syncOptions.filter_styles && !syncOptions.filter_brands) {
            countDiv.style.display = 'none';
            return;
        }
        
        countDiv.style.display = 'block';
        countValue.textContent = 'Hesaplanıyor...';
        countValue.className = 'badge bg-secondary';
        
        const response = await fetch('/api/products/count', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                ss_account_number: document.getElementById('ssAccountNumber').value,
                ss_api_key: document.getElementById('ssApiKey').value,
                sync_options: syncOptions
            })
        });
        
        const result = await response.json();
        if (result.status === 'success') {
            countValue.textContent = `${result.count.toLocaleString()} adet`;
            countValue.className = 'badge bg-success';
        } else {
            countValue.textContent = 'Hesaplanamadı';
            countValue.className = 'badge bg-warning';
        }
    } catch (error) {
        console.error('Product count error:', error);
        countValue.textContent = 'Hata';
        countValue.className = 'badge bg-danger';
    }
}

// Update auto sync filters display
async function updateAutoSyncFiltersDisplay() {
    const displayDiv = document.getElementById('autoSyncFiltersDisplay');
    if (!displayDiv) return;
    
    try {
        // Get saved sync options from database
        const response = await fetch('/api/config');
        const data = await response.json();
        
        if (data.sync_options && (data.sync_options.filter_categories || data.sync_options.filter_styles || data.sync_options.filter_brands)) {
            const categories = data.sync_options.filter_categories || [];
            const styles = data.sync_options.filter_styles || [];
            const brands = data.sync_options.filter_brands || [];
            
            const catCount = Array.isArray(categories) ? categories.length : (categories ? 1 : 0);
            const styleCount = Array.isArray(styles) ? styles.length : (styles ? 1 : 0);
            const brandCount = Array.isArray(brands) ? brands.length : (brands ? 1 : 0);
            
            displayDiv.innerHTML = `
                <div class="row">
                    <div class="col-md-6">
                        <p><strong>Seçilen Kategoriler:</strong> ${catCount} adet</p>
                        <p><strong>Seçilen Stiller:</strong> ${styleCount} adet</p>
                        <p><strong>Seçilen Markalar:</strong> ${brandCount} adet</p>
                    </div>
                    <div class="col-md-6">
                        <p><strong>Gerçek Ürün Sayısı:</strong> <span id="autoSyncProductCount" class="badge bg-secondary">Hesaplanıyor...</span></p>
                        <p><strong>Part Number:</strong> ${data.sync_options.filter_partnumber || 'Yok'}</p>
                        <p><strong>Depo:</strong> ${data.sync_options.filter_warehouses || 'Yok'}</p>
                        <p><strong>SKU:</strong> ${data.sync_options.filter_sku || 'Yok'}</p>
                    </div>
                </div>
            `;
            
            // Get actual count
            try {
                const countResponse = await fetch('/api/products/count', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        ss_account_number: document.getElementById('ssAccountNumber').value,
                        ss_api_key: document.getElementById('ssApiKey').value,
                        sync_options: data.sync_options
                    })
                });
                const countResult = await countResponse.json();
                if (countResult.status === 'success') {
                    const countSpan = document.getElementById('autoSyncProductCount');
                    if (countSpan) {
                        countSpan.textContent = `${countResult.count.toLocaleString()} adet`;
                        countSpan.className = 'badge bg-success';
                    }
                }
            } catch (e) {
                console.error('Auto sync count error:', e);
            }
        } else {
            displayDiv.innerHTML = '<p class="text-muted">Henüz filtre seçilmedi. Lütfen önce "Aktarım Seçenekleri" sekmesinden filtreleri seçin.</p>';
        }
    } catch (error) {
        console.error('Error updating auto sync filters display:', error);
        displayDiv.innerHTML = '<p class="text-danger">Filtre bilgileri yüklenirken hata oluştu.</p>';
    }
}

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
    // Get auto sync specific options
    const autoSyncOptions = {
        update_inventory: document.getElementById('autoSyncUpdateInventory').checked,
        update_prices: document.getElementById('autoSyncUpdatePrices').checked,
        update_images: document.getElementById('autoSyncUpdateImages').checked,
        create_new: document.getElementById('autoSyncCreateNew').checked,
        update_existing: document.getElementById('autoSyncUpdateExisting').checked,
        update_collections: document.getElementById('autoSyncUpdateCollections').checked
    };
    
    // Get base sync options (filters)
    const baseSyncOptions = getSyncOptions();
    
    // Merge options
    const syncOptions = {
        ...baseSyncOptions,
        // Override with auto sync specific options
        update_inventory: autoSyncOptions.update_inventory,
        update_prices: autoSyncOptions.update_prices,
        update_images: autoSyncOptions.update_images,
        create_new: autoSyncOptions.create_new,
        update_existing: autoSyncOptions.update_existing,
        sync_collections: autoSyncOptions.update_collections
    };
    
    const configData = {
        ss_account_number: document.getElementById('ssAccountNumber').value,
        ss_api_key: document.getElementById('ssApiKey').value,
        shopify_domain: document.getElementById('shopifyDomain').value,
        shopify_token: document.getElementById('shopifyToken').value,
        sync_options: syncOptions,
        auto_sync_options: autoSyncOptions,
        require_approval: document.getElementById('autoSyncRequireApproval').checked,
        interval_hours: parseInt(document.getElementById('autoSyncInterval').value)
    };
    
    if (!configData.ss_account_number || !configData.ss_api_key || 
        !configData.shopify_domain || !configData.shopify_token) {
        showAlert('Lütfen önce API bilgilerini yapılandırın', 'warning');
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
            showAlert(result.status === 'success' ? 'Otomatik güncelleme başlatıldı!' : result.message, 
                      result.status === 'success' ? 'success' : 'danger');
            loadAutoSyncStatus();
        } catch (error) {
            showAlert('Hata: ' + error.message, 'danger');
        }
    } else {
        try {
            await fetch('/api/auto-sync/stop', { method: 'POST' });
            showAlert('Otomatik güncelleme durduruldu', 'info');
            loadAutoSyncStatus();
        } catch (error) {
            showAlert('Hata: ' + error.message, 'danger');
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

// Show rollback last sync modal
function showRollbackLastSyncModal() {
    const modalElement = document.getElementById('rollbackLastSyncModal');
    if (!modalElement) {
        showAlert('Modal bulunamadı. Sayfayı yenileyin.', 'error');
        return;
    }
    
    const modal = new bootstrap.Modal(modalElement);
    modal.show();
    
    // Reset checkbox
    const checkbox = document.getElementById('confirmRollback');
    if (checkbox) {
        checkbox.checked = false;
        document.getElementById('rollbackConfirmBtn').disabled = true;
        
        // Enable/disable confirm button based on checkbox
        checkbox.onchange = function() {
            document.getElementById('rollbackConfirmBtn').disabled = !this.checked;
        };
    }
}

// Rollback last sync
async function rollbackLastSync() {
    try {
        const config = await fetch('/api/config').then(r => r.json());
        if (!config.shopify_config || !config.shopify_config.shop_domain || !config.shopify_config.access_token) {
            showAlert('Shopify bilgileri bulunamadı. Lütfen önce API ayarlarını kaydedin.', 'error');
            return;
        }
        
        const response = await fetch('/api/sync/rollback-last', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                shopify_domain: config.shopify_config.shop_domain,
                shopify_token: config.shopify_config.access_token
            })
        });
        
        const result = await response.json();
        if (result.status === 'success') {
            showAlert(`Başarılı: ${result.deleted} ürün silindi. ${result.errors.length > 0 ? 'Hatalar: ' + result.errors.join(', ') : ''}`, 'success');
            bootstrap.Modal.getInstance(document.getElementById('rollbackLastSyncModal')).hide();
        } else {
            showAlert('Hata: ' + result.message, 'error');
        }
    } catch (error) {
        showAlert('Hata: ' + error.message, 'error');
    }
}

// Show delete all modal
function showDeleteAllModal() {
    const modalElement = document.getElementById('deleteAllModal');
    if (!modalElement) {
        showAlert('Modal bulunamadı. Sayfayı yenileyin.', 'error');
        return;
    }
    
    const modal = new bootstrap.Modal(modalElement);
    modal.show();
    
    // Reset checkboxes
    const checkbox = document.getElementById('confirmDeleteAll');
    if (checkbox) {
        checkbox.checked = false;
        document.getElementById('deleteAllConfirmBtn').disabled = true;
        
        // Enable/disable confirm button based on checkbox
        checkbox.onchange = function() {
            document.getElementById('deleteAllConfirmBtn').disabled = !this.checked;
        };
    }
}

// Delete all Shopify data
async function deleteAllShopifyData() {
    try {
        const config = await fetch('/api/config').then(r => r.json());
        if (!config.shopify_config || !config.shopify_config.shop_domain || !config.shopify_config.access_token) {
            showAlert('Shopify bilgileri bulunamadı. Lütfen önce API ayarlarını kaydedin.', 'error');
            return;
        }
        
        const deleteProducts = document.getElementById('deleteProductsCheck').checked;
        const deleteCollections = document.getElementById('deleteCollectionsCheck').checked;
        
        if (!deleteProducts && !deleteCollections) {
            showAlert('Lütfen en az bir seçenek işaretleyin.', 'warning');
            return;
        }
        
        showAlert('Silme işlemi başlatıldı. Bu işlem biraz zaman alabilir...', 'info');
        
        const response = await fetch('/api/shopify/delete-all', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                shopify_domain: config.shopify_config.shop_domain,
                shopify_token: config.shopify_config.access_token,
                delete_products: deleteProducts,
                delete_collections: deleteCollections
            })
        });
        
        const result = await response.json();
        if (result.status === 'success') {
            showAlert(`Başarılı: ${result.deleted_products} ürün ve ${result.deleted_collections} collection silindi.`, 'success');
            bootstrap.Modal.getInstance(document.getElementById('deleteAllModal')).hide();
        } else {
            showAlert('Hata: ' + result.message, 'error');
        }
    } catch (error) {
        showAlert('Hata: ' + error.message, 'error');
    }
}
