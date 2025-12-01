# S&S Activewear API 403 Forbidden - Detaylı Çözüm

## Sorun: Test Bağlantısı Başarılı Ama Senkronizasyon Başarısız

Eğer "Test Connections" başarılı oluyor ama senkronizasyon sırasında 403 hatası alıyorsanız:

### Olası Nedenler:

1. **API Key İzinleri Eksik**
   - API Key'iniz categories endpoint'ine erişebiliyor
   - Ancak products endpoint'ine erişim izni olmayabilir
   - **Çözüm:** api@ssactivewear.com'a e-posta gönderin ve tüm endpoint'lere erişim talep edin

2. **Rate Limiting**
   - Çok fazla istek gönderiyorsunuz
   - API sizi geçici olarak engelliyor
   - **Çözüm:** Daha yavaş senkronizasyon yapın veya bekleyin

3. **API Key Formatı**
   - API Key'iniz belirli endpoint'ler için sınırlı olabilir
   - **Çözüm:** Tam erişimli bir API Key talep edin

## Hızlı Çözüm Adımları

### 1. API Key'i Doğrulayın
```
1. https://www.ssactivewear.com/api adresine gidin
2. API Key'inizi kontrol edin
3. Tüm endpoint'lere erişim izni olduğundan emin olun
```

### 2. Filtreleme Kullanın
Tüm ürünleri çekmek yerine, küçük bir filtre ile başlayın:

**Panel'de:**
- "Sync All Products" seçeneğini kapatın
- "Filter by Brand" alanına bir marka girin (örn: "Gildan")
- Veya "Filter by Part Number" alanına bir part number girin

Bu şekilde daha az ürün çekilir ve authentication sorunları daha erken tespit edilir.

### 3. API Key Yenileyin
Eğer sorun devam ederse:
1. api@ssactivewear.com'a e-posta gönderin
2. Hesap numaranızı belirtin: 599...
3. "Products endpoint'ine erişim sorunu yaşıyorum" yazın
4. Yeni bir API Key talep edin

### 4. Test Senaryosu

**Küçük bir test yapın:**
1. Panel'de "Filter by Part Number" alanına `00760` yazın
2. "Sync All Products" seçeneğini kapatın
3. "Start Sync" butonuna tıklayın
4. Eğer bu çalışırsa, API Key'iniz çalışıyor demektir
5. Sorun büyük veri setlerinde olabilir

## Alternatif Çözüm: Manuel API Testi

Python ile doğrudan test edin:

```python
from ss_api_client import SSActivewearClient

# API bilgilerinizi girin
client = SSActivewearClient("599...", "your-api-key")

# Küçük bir test
try:
    # Categories çalışıyor mu?
    categories = client.get_categories(limit=1)
    print("Categories OK")
    
    # Products çalışıyor mu?
    products = client.get_products(limit=1)
    print("Products OK")
    
    # Tüm ürünler çalışıyor mu?
    all_products = client.get_all_products()
    print(f"All products OK: {len(all_products)} products")
except Exception as e:
    print(f"Error: {e}")
```

Bu test hangi endpoint'te sorun olduğunu gösterir.

## Destek

Sorun devam ederse:
- **E-posta:** api@ssactivewear.com
- **Hesap No:** 599... (ilk 3 hane)
- **Sorun:** Products endpoint'ine erişim hatası
- **Hata:** 403 Forbidden


