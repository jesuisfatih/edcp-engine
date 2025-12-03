# 📦 Depo Bazlı Stok Sistemi - Kurulum Rehberi

## 🎯 Sistem Özeti

Bu sistem, Shopify ürün sayfalarında S&S Activewear depolarından gerçek zamanlı stok gösterimi ve çoklu depo siparişi sağlar.

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  S&S Activewear  │────▶│   EDCP Sunucu    │────▶│  Shopify Mağaza  │
│      API         │     │  (Her 2 saatte)  │     │   Ürün Sayfası   │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

---

## 📋 Kurulum Adımları

### ADIM 1: EDCP Sunucusunu Güncelle

```bash
# Sunucuya bağlan
ssh root@YOUR-SERVER-IP

# Projeyi güncelle
cd /opt/edcp
git pull origin main

# Veritabanı tablolarını oluştur
python3 -c "from database import init_database; init_database()"

# Servisi yeniden başlat
systemctl restart edcp
```

### ADIM 2: İlk Depo Stok Senkronizasyonunu Başlat

```bash
# EDCP web panelinden veya curl ile:
curl -X POST http://YOUR-SERVER:5000/api/warehouse-stock/sync

# Scheduler'ı başlat (her 2 saatte otomatik güncelleme):
curl -X POST http://YOUR-SERVER:5000/api/warehouse-stock/scheduler/start
```

### ADIM 3: API'yi Test Et

```bash
# Bir SKU için stok kontrolü:
curl http://YOUR-SERVER:5000/api/warehouse-stock/sku/B12279503

# Bir style için tüm stoklar:
curl http://YOUR-SERVER:5000/api/warehouse-stock/style/5000

# Senkronizasyon durumu:
curl http://YOUR-SERVER:5000/api/warehouse-stock/status
```

---

## 🛍️ Shopify Kurulumu

### Seçenek A: Direkt Tema Düzenleme (Basit)

1. **Shopify Admin > Online Store > Themes > Edit Code**

2. **Sections** klasöründe `main-product.liquid` dosyasını bul

3. Ürün bilgileri bölümünün altına şu kodu ekle:

```liquid
{% comment %} WAREHOUSE STOCK TABLE {% endcomment %}
<div id="warehouse-stock-app"></div>
<script src="https://YOUR-SERVER:5000/static/shopify/warehouse-stock.js"></script>
<script>
  initWarehouseStock({
    apiUrl: 'https://YOUR-SERVER:5000/api/warehouse-stock/style/',
    styleId: '{{ product.metafields.ssactivewear.styleid | default: product.handle }}'
  });
</script>
```

### Seçenek B: App Embed (Önerilen)

1. **Shopify Admin > Settings > Apps and sales channels > Develop apps**

2. Yeni bir app oluştur: "Warehouse Stock Display"

3. App Proxy ayarla:
   - Subpath prefix: `apps`
   - Subpath: `warehouse`
   - Proxy URL: `https://YOUR-SERVER:5000/apps/warehouse`

4. Theme Extension oluştur ve `warehouse-stock-snippet.liquid` dosyasını ekle

---

## 📊 API Endpoints

| Endpoint | Method | Açıklama |
|----------|--------|----------|
| `/api/warehouse-stock/sku/<sku>` | GET | Tek SKU için depo stokları |
| `/api/warehouse-stock/style/<style_id>` | GET | Tüm style için depo stokları |
| `/api/warehouse-stock/sync` | POST | Manuel senkronizasyon |
| `/api/warehouse-stock/status` | GET | Senkronizasyon durumu |
| `/api/warehouse-stock/scheduler/start` | POST | Otomatik sync başlat |
| `/api/warehouse-stock/scheduler/stop` | POST | Otomatik sync durdur |
| `/apps/warehouse/stock?sku=XXX` | GET | Shopify App Proxy endpoint |

---

## 🔄 Senkronizasyon Akışı

```
Her 2 Saatte:
1. S&S Activewear API'den inventory çek
2. Her SKU için tüm depo stokları al
3. warehouse_stock_cache tablosuna kaydet
4. Shopify'da stok güncel!
```

---

## 🛒 Sepete Ekleme Mantığı

Müşteri seçimlerini şöyle kaydediyoruz:

```javascript
// Sepete eklenen ürün
{
  id: 12345678,  // Shopify variant ID
  quantity: 18,  // Toplam miktar
  properties: {
    "_warehouse_orders": "DS:10|IL:5|PA:3",  // Depo:miktar
    "_color": "Pepper",
    "_fulfillment_note": "Split shipment from 3 warehouse(s)"
  }
}
```

---

## 📝 Order İşleme

Sipariş geldiğinde `line_item.properties` içinden:

```json
{
  "_warehouse_orders": "DS:10|IL:5|PA:3"
}
```

Bu bilgiyi kullanarak S&S'e doğru depolardan sipariş gönderebilirsiniz.

---

## ⚠️ Önemli Notlar

1. **CORS**: Shopify'dan API'ye erişim için CORS header'ları eklendi.

2. **Cache**: Stoklar 2 saatte bir güncellenir. Gerçek zamanlı değil.

3. **Rate Limit**: S&S API rate limit'ine dikkat edin.

4. **Metafield**: Ürünlerin `ssactivewear.styleid` metafield'ı olmalı.

---

## 🐛 Sorun Giderme

### Stoklar görünmüyor?
```bash
# Senkronizasyon çalıştı mı?
curl http://YOUR-SERVER:5000/api/warehouse-stock/status

# SKU var mı?
curl http://YOUR-SERVER:5000/api/warehouse-stock/sku/YOUR_SKU
```

### CORS hatası?
- Sunucu URL'sinin HTTPS olduğundan emin olun
- App Proxy kullanmayı deneyin

### Scheduler çalışmıyor?
```bash
# Durumu kontrol et
curl http://YOUR-SERVER:5000/api/warehouse-stock/status

# Yeniden başlat
curl -X POST http://YOUR-SERVER:5000/api/warehouse-stock/scheduler/start
```

---

## 📞 Destek

Sorularınız için: [EDCP Admin Panel](/settings)

