# Hızlı Başlangıç Kılavuzu

## 1. Kurulum

```bash
# Gereksinimleri yükleyin
pip install -r requirements.txt

# Ortam değişkenlerini ayarlayın
cp .env.example .env
# .env dosyasını düzenleyin (opsiyonel, sadece SECRET_KEY için)
```

## 2. API Bilgilerini Hazırlayın

### S&S Activewear API
1. Hesap numaranızı hazırlayın
2. API anahtarınızı alın:
   - https://www.ssactivewear.com/api adresinden
   - veya api@ssactivewear.com'a e-posta gönderin

### Shopify API
1. Shopify Admin paneline giriş yapın
2. Settings > Apps and sales channels > Develop apps
3. Yeni bir app oluşturun veya mevcut app'i kullanın
4. Admin API access token oluşturun
5. Şu izinleri verin:
   - `read_products`
   - `write_products`
   - `read_collections`
   - `write_collections`

## 3. Uygulamayı Başlatın

```bash
python app.py
```

Tarayıcıda açın: http://localhost:5000

## 4. İlk Kullanım

1. **API Bilgilerini Girin:**
   - S&S Activewear Account Number
   - S&S Activewear API Key
   - Shopify Shop Domain (örn: `my-shop.myshopify.com`)
   - Shopify Access Token

2. **Bağlantıları Test Edin:**
   - "Test Connections" butonuna tıklayın
   - Her iki API'nin de başarılı olduğundan emin olun

3. **Senkronizasyon Seçeneklerini Ayarlayın:**
   - Hangi özelliklerin senkronize edileceğini seçin
   - Filtreleme seçeneklerini ayarlayın (isteğe bağlı)

4. **Ürünleri Önizleyin (Opsiyonel):**
   - "Preview Products" ile ilk 10 ürünü görüntüleyin

5. **Senkronizasyonu Başlatın:**
   - "Start Sync" butonuna tıklayın
   - İlerlemeyi gerçek zamanlı olarak takip edin

## 5. Önemli Notlar

- İlk senkronizasyon uzun sürebilir (tüm ürünler için)
- Shopify API limitlerine dikkat edin (2 requests/second)
- Hata loglarını düzenli olarak kontrol edin
- Test için önce küçük bir filtre ile başlayın

## Sorun Giderme

### "Failed to connect to Shopify" hatası
- Shop domain formatını kontrol edin: `shop-name.myshopify.com`
- Access token'ın doğru olduğundan emin olun
- API izinlerini kontrol edin

### "API request failed" hatası (S&S)
- Account number ve API key'i kontrol edin
- API anahtarının aktif olduğundan emin olun

### Senkronizasyon çok yavaş
- Normal, Shopify API limitleri nedeniyle
- Büyük senkronizasyonlar saatler sürebilir



