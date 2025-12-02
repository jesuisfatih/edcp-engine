# Sorun Giderme Kılavuzu

## S&S Activewear API 403 Forbidden Hatası

Bu hata, kimlik doğrulama sorununu gösterir. Aşağıdaki adımları kontrol edin:

### 1. Account Number Kontrolü
- Account Number'ınızı doğru girdiğinizden emin olun
- Boşluk veya özel karakter olmamalı
- Sadece sayılar olmalı (örnek: `12345`)

### 2. API Key Kontrolü
- API Key'inizi doğru kopyaladığınızdan emin olun
- Başında/sonunda boşluk olmamalı
- API Key'in aktif olduğundan emin olun

### 3. API Key Nasıl Alınır?

**Yöntem 1: Web Sitesinden**
1. https://www.ssactivewear.com/api adresine gidin
2. "Don't have an API Key? Find it here" linkine tıklayın
3. Giriş yapın ve API Key'inizi görüntüleyin

**Yöntem 2: E-posta ile**
- api@ssactivewear.com adresine e-posta gönderin
- Hesap numaranızı belirtin
- API Key talebinde bulunun

### 4. API Key Formatı
- API Key genellikle uzun bir alfanumerik string'dir
- Örnek format: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6`

### 5. Yaygın Hatalar

❌ **Yanlış:**
- Account Number: ` 12345 ` (boşluklu)
- API Key: `abc123` (çok kısa, muhtemelen yanlış)

✅ **Doğru:**
- Account Number: `12345`
- API Key: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6` (uzun string)

### 6. Test Adımları

1. **API bilgilerini temizleyin:**
   - Account Number ve API Key alanlarını boşaltın
   - Sayfayı yenileyin

2. **Bilgileri tekrar girin:**
   - Account Number'ı manuel olarak yazın (kopyala-yapıştır yapmayın)
   - API Key'i kopyala-yapıştır yapın, ancak başında/sonunda boşluk olmadığından emin olun

3. **Test edin:**
   - "Test Connections" butonuna tıklayın
   - Hata mesajını okuyun

### 7. Hala Çalışmıyorsa

1. **API Key'i yenileyin:**
   - api@ssactivewear.com'a e-posta gönderin
   - Yeni bir API Key talep edin

2. **Hesap durumunu kontrol edin:**
   - Hesabınızın aktif olduğundan emin olun
   - API erişiminin açık olduğundan emin olun

3. **Destek ile iletişime geçin:**
   - api@ssactivewear.com
   - Hesap numaranızı ve sorununuzu açıklayın

## Shopify API Hataları

### "Failed to connect to Shopify" Hatası

1. **Shop Domain Formatını Kontrol Edin:**
   - ❌ Yanlış: `https://my-shop.myshopify.com`
   - ❌ Yanlış: `my-shop.com`
   - ✅ Doğru: `my-shop.myshopify.com`

2. **Access Token Kontrolü:**
   - Token'ın doğru kopyalandığından emin olun
   - Token'ın süresinin dolmadığından emin olun
   - Gerekli izinlerin verildiğinden emin olun:
     - `read_products`
     - `write_products`
     - `read_collections`
     - `write_collections`

3. **API İzinlerini Kontrol Edin:**
   - Shopify Admin > Settings > Apps and sales channels
   - App'inizi seçin
   - "Configure Admin API scopes" bölümünden izinleri kontrol edin

## Genel Sorunlar

### Port 5000 Kullanımda
```bash
# Windows'ta portu kullanan process'i bulun
netstat -ano | findstr :5000

# Process'i sonlandırın (PID'yi yukarıdaki komuttan alın)
taskkill /PID <PID> /F
```

### Python Modülleri Eksik
```bash
pip install -r requirements.txt
```

### Import Hataları
```bash
# Tüm bağımlılıkları yeniden yükleyin
pip install --upgrade -r requirements.txt
```

## Destek

Sorunlarınız için:
- S&S Activewear API: api@ssactivewear.com
- Shopify API: https://shopify.dev/docs/api/admin



