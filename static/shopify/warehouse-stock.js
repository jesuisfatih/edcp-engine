/**
 * WAREHOUSE STOCK TABLE - Shopify Integration
 * 
 * Bu script'i Shopify tema dosyasına ekleyerek depo bazlı stok tablosu gösterebilirsiniz.
 * 
 * Kullanım:
 * <div id="warehouse-stock-app"></div>
 * <script src="https://YOUR-SERVER/static/shopify/warehouse-stock.js"></script>
 * <script>
 *   initWarehouseStock({
 *     apiUrl: 'https://YOUR-SERVER/api/warehouse-stock/style/',
 *     styleId: '5000',
 *     variantId: 12345678  // Shopify variant ID
 *   });
 * </script>
 */

(function(global) {
  'use strict';

  // State
  let config = {};
  let stockData = {};
  let selectedColor = null;
  let orderQuantities = {};

  // Styles
  const styles = `
    .ws-container {
      border: 1px solid #e0e0e0;
      border-radius: 12px;
      padding: 20px;
      background: #fafafa;
      margin-top: 20px;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    .ws-title {
      margin: 0 0 20px 0;
      font-size: 18px;
      color: #333;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .ws-loading {
      text-align: center;
      padding: 40px;
    }
    .ws-spinner {
      width: 40px;
      height: 40px;
      border: 4px solid #f3f3f3;
      border-top: 4px solid #3498db;
      border-radius: 50%;
      animation: ws-spin 1s linear infinite;
      margin: 0 auto 15px;
    }
    @keyframes ws-spin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    .ws-error {
      background: #fff3f3;
      border: 1px solid #ffcdd2;
      padding: 15px;
      border-radius: 8px;
      color: #c62828;
    }
    .ws-colors {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 20px;
    }
    .ws-color-btn {
      padding: 8px 16px;
      border: 2px solid #ddd;
      border-radius: 20px;
      background: white;
      cursor: pointer;
      font-size: 13px;
      transition: all 0.2s;
    }
    .ws-color-btn:hover {
      border-color: #666;
    }
    .ws-color-btn.active {
      background: #1a365d;
      color: white;
      border-color: #1a365d;
    }
    .ws-matrix-container {
      overflow-x: auto;
      margin-bottom: 20px;
    }
    .ws-matrix {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }
    .ws-matrix th,
    .ws-matrix td {
      padding: 10px 8px;
      text-align: center;
      border: 1px solid #e0e0e0;
    }
    .ws-matrix th {
      background: #1a365d;
      color: white;
      font-weight: 600;
      min-width: 70px;
    }
    .ws-matrix th.sizes-header {
      background: #2d3748;
      min-width: 150px;
      text-align: left;
      padding-left: 15px;
    }
    .ws-matrix .size-price {
      font-size: 11px;
      color: #ffd700;
      display: block;
    }
    .ws-matrix tbody tr:nth-child(even) {
      background: #f7fafc;
    }
    .ws-matrix tbody tr:hover {
      background: #edf2f7;
    }
    .ws-matrix .warehouse-name {
      text-align: left;
      padding-left: 15px;
      font-weight: 500;
    }
    .ws-cell {
      position: relative;
    }
    .ws-qty-label {
      font-size: 11px;
      color: #666;
      display: block;
      margin-bottom: 4px;
    }
    .ws-qty-input {
      width: 50px;
      padding: 5px;
      text-align: center;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 13px;
    }
    .ws-qty-input:focus {
      border-color: #3182ce;
      outline: none;
      box-shadow: 0 0 0 2px rgba(49, 130, 206, 0.2);
    }
    .ws-qty-input.has-value {
      background: #e6fffa;
      border-color: #38b2ac;
    }
    .ws-out-of-stock {
      color: #a0aec0;
    }
    .ws-summary {
      background: white;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 15px;
      margin-bottom: 15px;
    }
    .ws-summary h4 {
      margin: 0 0 10px 0;
      font-size: 14px;
    }
    .ws-summary-item {
      display: flex;
      justify-content: space-between;
      padding: 5px 0;
      font-size: 13px;
      border-bottom: 1px dashed #e2e8f0;
    }
    .ws-total {
      display: flex;
      justify-content: space-between;
      margin-top: 10px;
      padding-top: 10px;
      border-top: 2px solid #1a365d;
      font-size: 16px;
    }
    .ws-total-price {
      color: #38a169;
    }
    .ws-add-btn {
      width: 100%;
      padding: 15px 30px;
      background: #38a169;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      transition: all 0.2s;
    }
    .ws-add-btn:hover:not(:disabled) {
      background: #2f855a;
      transform: translateY(-1px);
    }
    .ws-add-btn:disabled {
      background: #a0aec0;
      cursor: not-allowed;
    }
  `;

  // Main init function
  global.initWarehouseStock = function(options) {
    config = {
      apiUrl: options.apiUrl || '',
      styleId: options.styleId || '',
      variantId: options.variantId || null,
      containerId: options.containerId || 'warehouse-stock-app'
    };

    if (!config.apiUrl || !config.styleId) {
      console.error('WarehouseStock: apiUrl and styleId required');
      return;
    }

    injectStyles();
    renderContainer();
    loadStock();
  };

  function injectStyles() {
    if (document.getElementById('ws-styles')) return;
    const style = document.createElement('style');
    style.id = 'ws-styles';
    style.textContent = styles;
    document.head.appendChild(style);
  }

  function renderContainer() {
    const container = document.getElementById(config.containerId);
    if (!container) return;

    container.innerHTML = `
      <div class="ws-container">
        <h3 class="ws-title">📦 Depo Bazlı Stok ve Sipariş</h3>
        <div class="ws-loading" id="ws-loading">
          <div class="ws-spinner"></div>
          <p>Depo stokları yükleniyor...</p>
        </div>
        <div class="ws-error" id="ws-error" style="display: none;"></div>
        <div id="ws-content" style="display: none;">
          <div class="ws-colors" id="ws-colors"></div>
          <div class="ws-matrix-container">
            <table class="ws-matrix" id="ws-matrix">
              <thead><tr><th class="sizes-header">Sizes</th></tr></thead>
              <tbody id="ws-matrix-body"></tbody>
            </table>
          </div>
          <div class="ws-summary" id="ws-summary" style="display: none;">
            <h4>📋 Sipariş Özeti</h4>
            <div id="ws-summary-list"></div>
            <div class="ws-total">
              <strong>Toplam: <span id="ws-total-qty">0</span> adet</strong>
              <strong class="ws-total-price">$<span id="ws-total-price">0.00</span></strong>
            </div>
          </div>
          <button type="button" class="ws-add-btn" id="ws-add-btn" disabled>
            🛒 Sepete Ekle
          </button>
        </div>
      </div>
    `;
  }

  async function loadStock() {
    const loading = document.getElementById('ws-loading');
    const error = document.getElementById('ws-error');
    const content = document.getElementById('ws-content');

    try {
      const response = await fetch(config.apiUrl + config.styleId);
      const data = await response.json();

      if (data.status === 'success' && Object.keys(data.skus || {}).length > 0) {
        stockData = data.skus;
        loading.style.display = 'none';
        content.style.display = 'block';
        renderColors();
        setupAddToCart();
      } else {
        throw new Error('No stock data');
      }
    } catch (e) {
      console.error('WarehouseStock error:', e);
      loading.style.display = 'none';
      error.style.display = 'block';
      error.textContent = '⚠️ Stok bilgileri yüklenemedi. Lütfen sayfayı yenileyin.';
    }
  }

  function renderColors() {
    const container = document.getElementById('ws-colors');
    const colors = [...new Set(Object.values(stockData).map(s => s.color_name))].filter(Boolean);

    container.innerHTML = colors.map((color, i) => 
      `<button class="ws-color-btn ${i === 0 ? 'active' : ''}" data-color="${color}">${color}</button>`
    ).join('');

    container.querySelectorAll('.ws-color-btn').forEach(btn => {
      btn.addEventListener('click', () => selectColor(btn.dataset.color));
    });

    if (colors.length > 0) {
      selectColor(colors[0]);
    }
  }

  function selectColor(color) {
    selectedColor = color;
    orderQuantities = {};

    document.querySelectorAll('.ws-color-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.color === color);
    });

    renderMatrix();
    updateSummary();
  }

  function renderMatrix() {
    const colorSkus = Object.values(stockData).filter(s => s.color_name === selectedColor);
    if (colorSkus.length === 0) return;

    const sizes = [...new Set(colorSkus.map(s => s.size_name))];
    const allWarehouses = {};

    colorSkus.forEach(sku => {
      (sku.warehouses || []).forEach(wh => {
        if (wh.code && !allWarehouses[wh.code]) {
          allWarehouses[wh.code] = wh.name || wh.code;
        }
      });
    });

    const warehouseCodes = Object.keys(allWarehouses).sort();

    // Header
    const headerRow = document.querySelector('#ws-matrix thead tr');
    headerRow.innerHTML = '<th class="sizes-header">Sizes</th>' + sizes.map(size => {
      const sku = colorSkus.find(s => s.size_name === size);
      const price = sku?.warehouses?.[0]?.price || 0;
      return `<th>${size}<span class="size-price">$${price.toFixed(2)}</span></th>`;
    }).join('');

    // Body
    const tbody = document.getElementById('ws-matrix-body');
    tbody.innerHTML = warehouseCodes.map(whCode => {
      const whName = allWarehouses[whCode];

      const cells = sizes.map(size => {
        const sku = colorSkus.find(s => s.size_name === size);
        if (!sku) return '<td class="ws-out-of-stock">-</td>';

        const warehouse = (sku.warehouses || []).find(w => w.code === whCode);
        const qty = warehouse?.qty || 0;
        const skuId = sku.sku;

        if (qty === 0) {
          return `<td class="ws-cell ws-out-of-stock">
            <span class="ws-qty-label">Qty: 0</span>
            <input type="number" class="ws-qty-input" value="0" disabled>
          </td>`;
        }

        return `<td class="ws-cell">
          <span class="ws-qty-label">Qty: ${qty}</span>
          <input type="number" class="ws-qty-input" 
                 min="0" max="${qty}" value="0"
                 data-sku="${skuId}" 
                 data-warehouse="${whCode}"
                 data-price="${warehouse?.price || 0}"
                 data-max="${qty}">
        </td>`;
      }).join('');

      return `<tr><td class="warehouse-name">${whName}</td>${cells}</tr>`;
    }).join('');

    // Event listeners
    tbody.querySelectorAll('.ws-qty-input:not(:disabled)').forEach(input => {
      input.addEventListener('change', handleQtyChange);
      input.addEventListener('input', handleQtyChange);
    });
  }

  function handleQtyChange(e) {
    const input = e.target;
    const sku = input.dataset.sku;
    const warehouse = input.dataset.warehouse;
    const price = parseFloat(input.dataset.price);
    const max = parseInt(input.dataset.max);
    let qty = parseInt(input.value) || 0;

    if (qty < 0) qty = 0;
    if (qty > max) qty = max;
    input.value = qty;

    const key = `${sku}_${warehouse}`;
    if (qty > 0) {
      orderQuantities[key] = { sku, warehouse, qty, price };
      input.classList.add('has-value');
    } else {
      delete orderQuantities[key];
      input.classList.remove('has-value');
    }

    updateSummary();
  }

  function updateSummary() {
    const summary = document.getElementById('ws-summary');
    const list = document.getElementById('ws-summary-list');
    const totalQtyEl = document.getElementById('ws-total-qty');
    const totalPriceEl = document.getElementById('ws-total-price');
    const addBtn = document.getElementById('ws-add-btn');

    const orders = Object.values(orderQuantities);

    if (orders.length === 0) {
      summary.style.display = 'none';
      addBtn.disabled = true;
      return;
    }

    summary.style.display = 'block';
    addBtn.disabled = false;

    let totalQty = 0;
    let totalPrice = 0;

    list.innerHTML = orders.map(order => {
      const subtotal = order.qty * order.price;
      totalQty += order.qty;
      totalPrice += subtotal;
      return `<div class="ws-summary-item">
        <span>${order.warehouse}: ${order.qty} adet</span>
        <span>$${subtotal.toFixed(2)}</span>
      </div>`;
    }).join('');

    totalQtyEl.textContent = totalQty;
    totalPriceEl.textContent = totalPrice.toFixed(2);
  }

  function setupAddToCart() {
    const btn = document.getElementById('ws-add-btn');
    btn.addEventListener('click', addToCart);
  }

  async function addToCart() {
    const orders = Object.values(orderQuantities);
    if (orders.length === 0) return;

    const btn = document.getElementById('ws-add-btn');
    btn.disabled = true;
    btn.textContent = 'Ekleniyor...';

    try {
      const warehouseBreakdown = orders.map(o => `${o.warehouse}:${o.qty}`).join('|');
      const totalQty = orders.reduce((sum, o) => sum + o.qty, 0);

      const response = await fetch('/cart/add.js', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          id: config.variantId,
          quantity: totalQty,
          properties: {
            '_warehouse_orders': warehouseBreakdown,
            '_color': selectedColor,
            '_fulfillment_note': `Split shipment from ${orders.length} warehouse(s)`
          }
        })
      });

      if (response.ok) {
        btn.textContent = '✓ Sepete Eklendi!';
        setTimeout(() => {
          window.location.href = '/cart';
        }, 1000);
      } else {
        throw new Error('Failed');
      }
    } catch (e) {
      console.error('Add to cart error:', e);
      btn.textContent = 'Hata! Tekrar Deneyin';
      btn.disabled = false;
    }
  }

})(window);

