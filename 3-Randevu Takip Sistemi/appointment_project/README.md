# 🗓️ Randevu Yönetim Sistemi

Bu proje **Django** kullanılarak geliştirilmiş basit bir randevu yönetim uygulamasıdır.  
Kullanıcılar giriş yapıp farklı kategorilerde randevu alabilir ve uygunluk durumunu görebilirler.  

---

## 🚀 Özellikler
- ✅ Kullanıcı kayıt olma ve giriş yapma (Django Auth ile)  
- ✅ Hastane için poliklinik seçerek randevu alma  
- ✅ Spor randevusu oluşturma  
- ✅ Diş kliniği randevusu oluşturma  
- ✅ Kuaför randevusu oluşturma  
- ✅ Çakışan saatlerde randevu alınamaması (doluluk kontrolü)  
- ✅ Tüm randevuların listelenmesi  

---

## 🛠 Kullanılan Teknolojiler
- [Python](https://www.python.org/) 3.x  
- [Django](https://www.djangoproject.com/) 4.x  
- SQLite (varsayılan veritabanı)  
- Django Messages Framework (geri bildirim mesajları için)  
- Bootstrap (form stilleri için `form-control` sınıfı)  

---

⚙️ Kurulum

Projeyi klonla:
git clone https://github.com/kullaniciadi/proje-adi.git
cd proje-adi

Sanal ortam oluştur ve aktif et:
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux / Mac


Gerekli bağımlılıkları yükle:
pip install django

Veritabanını migrate et:
python manage.py migrate

Sunucuyu çalıştır:
python manage.py runserver

📌 Notlar
Randevu alınırken aynı gün ve saat doluysa hata mesajı gösterilir.
Tüm alanların doldurulması zorunludur.
Kullanıcı giriş yapmadan randevu ekranlarına erişemez. (@login_required)

✨ Katkı
Projeye katkı yapmak için fork edip pull request gönderebilirsiniz 😊