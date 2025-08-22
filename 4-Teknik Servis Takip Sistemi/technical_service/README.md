# 🛠️ Teknik Servis Takip Sistemi

Bu proje, **Django** kullanılarak geliştirilmiş bir **Teknik Servis Yönetim Sistemi**dir.  
Kullanıcılar cihaz arızalarını sisteme kaydedebilir, teknik servis personeli ise bu cihazların durumunu yönetebilir.  
Böylece hem müşteri hem de servis tarafı için uçtan uca cihaz takibi sağlanır.  

---

## 🚀 Özellikler

- 🔐 **Kullanıcı Yönetimi**
  - Kullanıcı kayıt & giriş sistemi (e-posta tabanlı giriş)
  - Telefon numarası ile kayıt olma
  - Kullanıcı grupları:  
    - **Müşteriler** → Cihazlarını kaydedebilir ve durumlarını takip edebilir  
    - **Teknik Servis Elemanları** → Tüm cihazları görüntüleyebilir, durum güncellemesi yapabilir  

- 📱 **Cihaz Takibi**
  - Bilgisayar (masaüstü & laptop)
  - Akıllı Telefon
  - Akıllı Saat
  - Televizyon
  - Oyun Ekipmanları
  - Tablet

- 🔄 **Durum Yönetimi**
  - Beklemede
  - İşleme Alındı
  - Hata Giderildi

- ✅ **Diğer Özellikler**
  - Django Messages Framework ile başarılı/başarısız işlem bildirimleri
  - Kullanıcıya özel cihaz listesi
  - Teknik servis ekranında cihazların durumunu topluca güncelleme  

---

## 🛠 Kullanılan Teknolojiler

- [Python](https://www.python.org/) 3.x  
- [Django](https://www.djangoproject.com/) 4.x  
- SQLite (varsayılan veritabanı)  
- Django Auth (kullanıcı yönetimi)  
- Django Groups & Permissions (rol bazlı erişim)  
- Bootstrap (form & UI için)  

---

⚙️ Kurulum

📥 Projeyi klonla:
git clone https://github.com/kullaniciadi/teknik-servis-takip.git
cd teknik-servis-takip

🌍 Sanal ortam oluştur ve aktif et:
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux / Mac

📦 Bağımlılıkları yükle:
pip install django

🗄 Veritabanı migrasyonlarını çalıştır:
python manage.py migrate

👤 Süper kullanıcı oluştur:
python manage.py createsuperuser

▶️ Sunucuyu başlat:
python manage.py runserver

👤 Müşteri Paneli

Giriş yaptıktan sonra cihaz kaydı yapabilir:
/computer/ → Bilgisayar ekleme
/smart_phone/ → Telefon ekleme
/smart_watch/ → Akıllı saat ekleme
/tv/ → Televizyon ekleme
/player_equipment/ → Oyun ekipmanı ekleme
/tablet/ → Tablet ekleme
Kendi cihazlarının durumunu /customer_devices/ ekranından takip edebilir.

🛠 Teknik Servis Paneli
Teknik Servis Elemanları grubundaki kullanıcılar giriş yaptığında /defective_devices/ sayfasına yönlendirilir.
Burada tüm cihazları listeleyip, durum güncellemesi yapabilirler.

📊 Örnek Senaryo

Kullanıcı giriş yapar ve bilgisayar arızası kaydeder.
Teknik servis elemanı sisteme giriş yapar, cihazı listede görür.
Durumu "İşleme Alındı" → "Hata Giderildi" olarak günceller.
Kullanıcı, kendi cihaz listesinde güncel durumu görür. ✅

📌 Notlar

Tüm cihaz kayıtları ilgili kullanıcıya bağlıdır (ForeignKey(User)).
Teknik servis yetkisi Django Admin Panelinden kullanıcıyı Teknik Servis Elemanları grubuna ekleyerek verilir.
Hatalı ya da eksik alan doldurulduğunda kullanıcıya mesaj gösterilir.

✨ Katkı

Projeye katkıda bulunmak için:
Bu repoyu fork edin
Yeni bir branch oluşturun (feature/ozellik-adi)
Değişikliklerinizi commit edin
Pull Request gönderin 🚀