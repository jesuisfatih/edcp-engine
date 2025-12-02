/**
 * Product Search & Preview Module
 * E-commerce style product search and detail view
 */

(function() {
    let searchTimeout = null;
    let currentOffset = 0;
    let currentQuery = '';
    let isLoading = false;
    
    // Initialize on DOM ready
    document.addEventListener('DOMContentLoaded', function() {
        initProductSearch();
    });
    
    function initProductSearch() {
        const searchInput = document.getElementById('productSearchInput');
        const searchBtn = document.getElementById('productSearchBtn');
        const loadMoreBtn = document.getElementById('loadMoreBtn');
        
        if (searchInput) {
            // Live search with debounce
            searchInput.addEventListener('input', function() {
                clearTimeout(searchTimeout);
                searchTimeout = setTimeout(() => {
                    const query = this.value.trim();
                    if (query.length >= 2) {
                        currentOffset = 0;
                        currentQuery = query;
                        searchProducts(query, false);
                    } else if (query.length === 0) {
                        showInitialState();
                    }
                }, 500);
            });
            
            // Enter key search
            searchInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    clearTimeout(searchTimeout);
                    const query = this.value.trim();
                    if (query.length >= 2) {
                        currentOffset = 0;
                        currentQuery = query;
                        searchProducts(query, false);
                    }
                }
            });
        }
        
        if (searchBtn) {
            searchBtn.addEventListener('click', function() {
                const query = searchInput.value.trim();
                if (query.length >= 2) {
                    currentOffset = 0;
                    currentQuery = query;
                    searchProducts(query, false);
                }
            });
        }
        
        if (loadMoreBtn) {
            loadMoreBtn.addEventListener('click', function() {
                if (currentQuery && !isLoading) {
                    searchProducts(currentQuery, true);
                }
            });
        }
    }
    
    function searchProducts(query, append = false) {
        if (isLoading) return;
        isLoading = true;
        
        if (!append) {
            showLoadingState();
        }
        
        fetch('/api/search-products', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                query: query,
                limit: 24,
                offset: append ? currentOffset : 0
            })
        })
        .then(response => response.json())
        .then(data => {
            isLoading = false;
            
            if (data.status === 'success') {
                if (data.results.length === 0 && !append) {
                    showNoResults();
                } else {
                    if (append) {
                        appendResults(data.results);
                    } else {
                        showResults(data.results, data.total);
                    }
                    currentOffset = append ? currentOffset + data.results.length : data.results.length;
                    
                    // Show/hide load more button
                    const loadMoreContainer = document.getElementById('loadMoreContainer');
                    if (loadMoreContainer) {
                        loadMoreContainer.style.display = data.hasMore ? 'block' : 'none';
                    }
                }
                
                // Update result count
                const countEl = document.getElementById('searchResultCount');
                if (countEl) {
                    countEl.textContent = `${data.total} sonuç bulundu`;
                }
            } else {
                showError(data.message);
            }
        })
        .catch(error => {
            isLoading = false;
            console.error('Search error:', error);
            showError('Arama sırasında bir hata oluştu');
        });
    }
    
    function showLoadingState() {
        document.getElementById('searchInitialState').style.display = 'none';
        document.getElementById('noResultsMessage').style.display = 'none';
        document.getElementById('searchResultsContainer').style.display = 'none';
        document.getElementById('searchLoadingSpinner').style.display = 'block';
    }
    
    function showInitialState() {
        document.getElementById('searchLoadingSpinner').style.display = 'none';
        document.getElementById('noResultsMessage').style.display = 'none';
        document.getElementById('searchResultsContainer').style.display = 'none';
        document.getElementById('searchInitialState').style.display = 'block';
        document.getElementById('searchResultCount').textContent = '';
    }
    
    function showNoResults() {
        document.getElementById('searchLoadingSpinner').style.display = 'none';
        document.getElementById('searchInitialState').style.display = 'none';
        document.getElementById('searchResultsContainer').style.display = 'none';
        document.getElementById('noResultsMessage').style.display = 'block';
    }
    
    function showResults(results, total) {
        document.getElementById('searchLoadingSpinner').style.display = 'none';
        document.getElementById('searchInitialState').style.display = 'none';
        document.getElementById('noResultsMessage').style.display = 'none';
        document.getElementById('searchResultsContainer').style.display = 'block';
        
        const grid = document.getElementById('searchResultsGrid');
        grid.innerHTML = results.map(product => createProductCard(product)).join('');
    }
    
    function appendResults(results) {
        const grid = document.getElementById('searchResultsGrid');
        grid.innerHTML += results.map(product => createProductCard(product)).join('');
    }
    
    function showError(message) {
        document.getElementById('searchLoadingSpinner').style.display = 'none';
        alert('Hata: ' + message);
    }
    
    function createProductCard(product) {
        const imageUrl = product.image || 'https://via.placeholder.com/200x200?text=No+Image';
        const price = product.basePrice ? `$${parseFloat(product.basePrice).toFixed(2)}` : 'Fiyat yok';
        
        return `
            <div class="col-lg-3 col-md-4 col-sm-6 mb-4">
                <div class="card product-card" onclick="window.showProductDetail('${product.styleID}')">
                    <img src="${imageUrl}" class="product-card-img" alt="${product.styleName}" 
                         onerror="this.src='https://via.placeholder.com/200x200?text=No+Image'">
                    <div class="product-card-body">
                        <div class="product-card-brand">${product.brandName || ''}</div>
                        <div class="product-card-title">${product.title || product.styleName}</div>
                        <div class="product-card-style">${product.styleName}</div>
                        <div class="d-flex justify-content-between align-items-center mt-2">
                            <span class="product-card-price">${price}</span>
                            <span class="product-card-variants">
                                <i class="fas fa-palette"></i> ${product.colorCount || 0}
                                <i class="fas fa-ruler ms-2"></i> ${product.sizeCount || 0}
                            </span>
                        </div>
                        <div class="text-muted mt-1" style="font-size: 11px;">
                            ${product.variantCount} varyant
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
    
    // Show product detail modal
    window.showProductDetail = function(styleId) {
        const modal = new bootstrap.Modal(document.getElementById('productDetailModal'));
        const content = document.getElementById('productDetailContent');
        
        content.innerHTML = `
            <div class="text-center py-5">
                <div class="spinner-border text-primary" role="status" style="width: 3rem; height: 3rem;">
                    <span class="visually-hidden">Yükleniyor...</span>
                </div>
                <p class="mt-3 text-muted">Ürün detayları yükleniyor...</p>
            </div>
        `;
        
        modal.show();
        
        fetch(`/api/product-detail/${styleId}`)
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    renderProductDetail(data.product);
                } else {
                    content.innerHTML = `
                        <div class="alert alert-danger m-4">
                            <i class="fas fa-exclamation-triangle"></i> ${data.message}
                        </div>
                    `;
                }
            })
            .catch(error => {
                console.error('Error loading product:', error);
                content.innerHTML = `
                    <div class="alert alert-danger m-4">
                        <i class="fas fa-exclamation-triangle"></i> Ürün detayları yüklenemedi
                    </div>
                `;
            });
    };
    
    function renderProductDetail(product) {
        const content = document.getElementById('productDetailContent');
        const modalTitle = document.getElementById('productDetailModalTitle');
        
        modalTitle.innerHTML = `<i class="fas fa-box"></i> ${product.brandName} ${product.styleName}`;
        
        // Get first color images
        const firstColor = product.colors[0] || 'Default';
        const images = product.images[firstColor] || Object.values(product.images)[0] || [];
        const mainImage = images[0] || 'https://via.placeholder.com/500x500?text=No+Image';
        
        // Price display
        const priceDisplay = product.minPrice === product.maxPrice
            ? `$${product.minPrice.toFixed(2)}`
            : `$${product.minPrice.toFixed(2)} - $${product.maxPrice.toFixed(2)}`;
        
        content.innerHTML = `
            <div class="product-detail-container">
                <div class="row">
                    <!-- Left: Images -->
                    <div class="col-lg-5">
                        <div class="product-gallery">
                            <img src="${mainImage}" class="product-main-image" id="mainProductImage"
                                 onerror="this.src='https://via.placeholder.com/500x500?text=No+Image'">
                            <div class="product-thumbnails" id="productThumbnails">
                                ${renderThumbnails(product.images)}
                            </div>
                            
                            <!-- Color Selection -->
                            <div class="mt-4">
                                <label class="form-label fw-bold">Renk Seçimi (${product.colors.length})</label>
                                <div class="d-flex flex-wrap gap-2" id="colorSelector">
                                    ${product.colors.map((color, idx) => `
                                        <button class="btn btn-sm ${idx === 0 ? 'btn-primary' : 'btn-outline-secondary'}" 
                                                onclick="window.selectProductColor('${color}', ${JSON.stringify(product.images).replace(/"/g, '&quot;')})">
                                            ${color}
                                        </button>
                                    `).join('')}
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Right: Info -->
                    <div class="col-lg-7">
                        <div class="product-info-section">
                            <div class="product-brand-label">${product.brandName}</div>
                            <h1 class="product-title-large">${product.title || product.styleName}</h1>
                            <span class="product-style-badge">Style: ${product.styleName}</span>
                            
                            <div class="product-price-large">${priceDisplay}</div>
                            
                            ${product.description ? `
                                <div class="mb-4">
                                    <p class="text-muted">${product.description}</p>
                                </div>
                            ` : ''}
                            
                            <!-- Quick Stats -->
                            <div class="product-meta-grid">
                                <div class="product-meta-item">
                                    <div class="product-meta-label">Toplam Varyant</div>
                                    <div class="product-meta-value">${product.totalVariants}</div>
                                </div>
                                <div class="product-meta-item">
                                    <div class="product-meta-label">Renk Sayısı</div>
                                    <div class="product-meta-value">${product.colors.length}</div>
                                </div>
                                <div class="product-meta-item">
                                    <div class="product-meta-label">Beden Sayısı</div>
                                    <div class="product-meta-value">${product.sizes.length}</div>
                                </div>
                                <div class="product-meta-item">
                                    <div class="product-meta-label">Bedenler</div>
                                    <div class="product-meta-value">${product.sizes.join(', ')}</div>
                                </div>
                            </div>
                            
                            <!-- Variants Table -->
                            <div class="mt-4">
                                <h5 class="mb-3"><i class="fas fa-list"></i> Varyantlar (SKU Listesi)</h5>
                                <div style="max-height: 400px; overflow-y: auto;">
                                    <table class="table table-sm table-hover variant-table">
                                        <thead>
                                            <tr>
                                                <th>SKU</th>
                                                <th>Renk</th>
                                                <th>Beden</th>
                                                <th>Fiyat</th>
                                                <th>Stok</th>
                                                <th>Ağırlık</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            ${product.variants.map(v => `
                                                <tr>
                                                    <td><code>${v.sku}</code></td>
                                                    <td>${v.colorName}</td>
                                                    <td>${v.sizeName}</td>
                                                    <td>$${(v.piecePrice || 0).toFixed(2)}</td>
                                                    <td>
                                                        <span class="stock-badge ${getStockClass(v.inventory)}">
                                                            ${v.inventory}
                                                        </span>
                                                    </td>
                                                    <td>${v.weight ? v.weight + ' lb' : '-'}</td>
                                                </tr>
                                            `).join('')}
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                            
                            <!-- Metafields Section -->
                            <div class="metafield-section">
                                <h5 class="mb-3"><i class="fas fa-database"></i> Tüm Metafield'lar (API Verileri)</h5>
                                <div class="metafield-grid">
                                    ${Object.entries(product.metafields).map(([key, value]) => `
                                        <div class="metafield-item">
                                            <div class="metafield-key">${formatMetafieldKey(key)}</div>
                                            <div class="metafield-value">${formatMetafieldValue(value)}</div>
                                        </div>
                                    `).join('')}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
    
    function renderThumbnails(images) {
        let html = '';
        let index = 0;
        
        for (const [color, urls] of Object.entries(images)) {
            for (const url of urls) {
                html += `
                    <img src="${url}" 
                         class="product-thumbnail ${index === 0 ? 'active' : ''}" 
                         onclick="window.selectThumbnail(this, '${url}')"
                         onerror="this.style.display='none'"
                         title="${color}">
                `;
                index++;
                if (index >= 8) break; // Max 8 thumbnails initially
            }
            if (index >= 8) break;
        }
        
        return html;
    }
    
    window.selectThumbnail = function(element, url) {
        document.querySelectorAll('.product-thumbnail').forEach(el => el.classList.remove('active'));
        element.classList.add('active');
        document.getElementById('mainProductImage').src = url;
    };
    
    window.selectProductColor = function(color, images) {
        const colorImages = images[color] || [];
        if (colorImages.length > 0) {
            document.getElementById('mainProductImage').src = colorImages[0];
            
            // Update thumbnails
            const thumbContainer = document.getElementById('productThumbnails');
            thumbContainer.innerHTML = colorImages.map((url, idx) => `
                <img src="${url}" 
                     class="product-thumbnail ${idx === 0 ? 'active' : ''}" 
                     onclick="window.selectThumbnail(this, '${url}')"
                     onerror="this.style.display='none'"
                     title="${color}">
            `).join('');
        }
        
        // Update button states
        document.querySelectorAll('#colorSelector button').forEach(btn => {
            btn.classList.remove('btn-primary');
            btn.classList.add('btn-outline-secondary');
        });
        event.target.classList.remove('btn-outline-secondary');
        event.target.classList.add('btn-primary');
    };
    
    function getStockClass(stock) {
        if (stock === 0) return 'stock-out';
        if (stock < 10) return 'stock-low';
        if (stock < 50) return 'stock-medium';
        return 'stock-high';
    }
    
    function formatMetafieldKey(key) {
        return key
            .replace(/([A-Z])/g, ' $1')
            .replace(/^./, str => str.toUpperCase())
            .trim();
    }
    
    function formatMetafieldValue(value) {
        if (typeof value === 'boolean') {
            return value ? '✓ Evet' : '✗ Hayır';
        }
        if (typeof value === 'number') {
            return value.toLocaleString();
        }
        return String(value);
    }
    
})();

