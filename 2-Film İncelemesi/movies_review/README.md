# 🎬 Film İnceleme Uygulaması

Bu proje **Django** ile geliştirilmiş basit bir film inceleme uygulamasıdır.  
Kullanıcılar filmleri görüntüleyebilir, detay sayfasına girip yorum ve puan ekleyebilir.  

---

## 🚀 Özellikler
- ✅ Film ekleme (isim, tür, yıl, yönetmen, afiş/poster)  
- ✅ Filmlerin listelenmesi  
- ✅ Film detay sayfasında yorumların görüntülenmesi  
- ✅ Yorum ekleme (yorum + 1–10 arası puan)  
- ✅ Film silindiğinde yorumların da otomatik silinmesi (CASCADE)  

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

Gerekli bağımlılıkları yükle:
pip install django pillow
(pillow resim yüklemeleri için gerekli.)

Veritabanını migrate et:
python manage.py migrate

Sunucuyu çalıştır:
python manage.py runserver

📌 Notlar
poster alanı opsiyoneldir, yüklenmezse boş kalır.
rating alanı 1 ile 10 arasında değer alır (ondalık destekler).
get_object_or_404 ile hatalı ID girilirse 404 döner.

✨ Katkı
Fork ve PR kabul edilir 😊