# 📚 Kitap Yönetim Sistemi

Bu proje **Django** ile geliştirilmiş basit bir kitap yönetim uygulamasıdır.  
Uygulama üzerinden kitap ekleme, listeleme, güncelleme ve silme işlemleri yapılabilir.  

---

## 🚀 Özellikler
- ✅ Kitap ekleme (isim, yazar, sayfa sayısı, tür, yayın yılı)
- ✅ Kitapları listeleme
- ✅ Kitap bilgilerini düzenleme
- ✅ Kitap silme
- ✅ Django mesaj sistemi ile kullanıcıya bildirim gösterme

---

## 🛠 Kullanılan Teknolojiler
- [Python](https://www.python.org/) 3.x
- [Django](https://www.djangoproject.com/) 4.x
- SQLite (varsayılan veritabanı)

---

⚙️ Kurulum

Projeyi klonla:
git clone https://github.com/kullaniciadi/proje-adi.git
cd proje-adi

Sanal ortam oluştur ve aktif et:
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux / Mac

Bağımlılıkları yükle:
pip install django

Veritabanını migrate et:
python manage.py migrate

Sunucuyu çalıştır:
python manage.py runserver

📌 Notlar
publication_date alanı için 1900’den bugüne kadar olan yıllar otomatik olarak seçim kutusunda gösterilir.
Django’nun messages framework’ü ile işlem başarı/hata durumları kullanıcıya bildirilir.

✨ Katkı
Fork ve PR kabul edilir 😊