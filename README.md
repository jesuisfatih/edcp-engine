# S&S Activewear to Shopify Sync Bot

Ultra gelişmiş bir Python botu ve web paneli ile S&S Activewear API'sinden Shopify'a ürün senkronizasyonu yapın.

## Özellikler

- ✅ **Tam API Entegrasyonu**: S&S Activewear API'sinin tüm özelliklerini destekler
- ✅ **Shopify 2025 Uyumlu**: En güncel Shopify Admin API (2025-01) kullanır
- ✅ **Gelişmiş Kontrol Paneli**: Modern ve kullanıcı dostu web arayüzü
- ✅ **Esnek Senkronizasyon Seçenekleri**:
  - Yeni ürün oluşturma
  - Mevcut ürünleri güncelleme
  - Koleksiyon yönetimi (otomatik oluşturma)
  - Etiket senkronizasyonu
  - Filtreleme seçenekleri (Marka, Stil, Part Number)
- ✅ **Gerçek Zamanlı İlerleme Takibi**: Canlı istatistikler ve hata logları
- ✅ **Bağlantı Testi**: API bağlantılarını test edin

## Kurulum

1. **Gereksinimleri yükleyin:**
```bash
pip install -r requirements.txt
```

2. **Ortam değişkenlerini ayarlayın:**
```bash
cp .env.example .env
# .env dosyasını düzenleyin ve SECRET_KEY'i değiştirin
```

3. **Uygulamayı başlatın:**
```bash
python app.py
```

4. **Tarayıcıda açın:**
```
http://localhost:5000
```

## Kullanım

### 1. API Yapılandırması

**S&S Activewear API:**
- Account Number: Hesap numaranız
- API Key: API anahtarınız ([Buradan alın](https://www.ssactivewear.com/api) veya api@ssactivewear.com'a e-posta gönderin)

**Shopify API:**
- Shop Domain: `your-shop.myshopify.com` formatında
- Access Token: Shopify Admin API erişim token'ınız (2025-01 API versiyonu)

### 2. Senkronizasyon Seçenekleri

- **Sync All Products**: Tüm ürünleri senkronize et
- **Create New Products**: Yeni ürünler oluştur
- **Update Existing Products**: Mevcut ürünleri güncelle
- **Sync Collections**: Koleksiyonları senkronize et
- **Create Collections if Not Exists**: Koleksiyon yoksa oluştur
- **Create Brand Collections**: Marka koleksiyonları oluştur
- **Sync Tags**: Etiketleri senkronize et
- **Set Products as Active**: Ürünleri aktif olarak ayarla

### 3. Filtreleme Seçenekleri

- **Filter by Style**: Belirli stilleri filtrele (örn: `00760, Gildan 5000`)
- **Filter by Part Number**: Part number'a göre filtrele
- **Filter by Brand**: Markaya göre filtrele

### 4. Senkronizasyonu Başlatma

1. API bilgilerini girin ve "Save Configuration" butonuna tıklayın
2. "Test Connections" ile bağlantıları test edin
3. Senkronizasyon seçeneklerini yapılandırın
4. "Start Sync" butonuna tıklayın
5. İlerlemeyi gerçek zamanlı olarak takip edin

## API Endpoints

### S&S Activewear API Desteklenen Endpoint'ler

- ✅ Categories (`/v2/categories/`)
- ✅ Brands (`/v2/Brands/`)
- ✅ Styles (`/v2/styles/`)
- ✅ Products (`/v2/products/`)
- ✅ Inventory (`/v2/inventory/`)
- ✅ Specs (`/v2/specs/`)

### Shopify API Özellikleri

- ✅ Ürün oluşturma ve güncelleme
- ✅ Variant yönetimi
- ✅ Görsel yönetimi
- ✅ Koleksiyon yönetimi
- ✅ Etiket yönetimi
- ✅ Envanter yönetimi

## Güvenlik Notları

- `.env` dosyasını asla Git'e commit etmeyin
- API anahtarlarınızı güvende tutun
- Production ortamında `SECRET_KEY`'i mutlaka değiştirin
- HTTPS kullanın (production için)

## Sorun Giderme

### Bağlantı Hataları

- API bilgilerinizi kontrol edin
- "Test Connections" butonunu kullanarak bağlantıları test edin
- Firewall ayarlarınızı kontrol edin

### Senkronizasyon Hataları

- Hata loglarını kontrol edin
- Shopify API limitlerini kontrol edin
- Ürün verilerinin formatını kontrol edin

## Lisans

Bu proje özel kullanım içindir.

## Destek

Sorularınız için:
- S&S Activewear API: api@ssactivewear.com
- Shopify API: [Shopify Developer Docs](https://shopify.dev/docs/api/admin)


