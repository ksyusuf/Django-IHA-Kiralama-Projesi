# İHA Kiralama Projesi

Bu proje, Django ve PostgreSQL kullanılarak geliştirilen bir İnsansız Hava Aracı (İHA) kiralama web uygulamasıdır.
Projede, üyelik sistemi ve kiralama işlemleri ypaılabilmektedir.

## Gereksinimler

- Python 3.x
- Django
- PostgreSQL

## Kurulum

1. Proje dosyalarını klonlayın:

```
git clone https://github.com/kullanici/ihakiralama-projesi.git

```
2. Virtual environment oluşturun (isteğe bağlı):
    
```
python3 -m venv .venv

```

3. Virtual environment'ı aktive edin:

```
source .venv/bin/activate.bat

```
4. Gerekli kütüphaneleri yükleyin:


```
pip install -r requirements.txt

```
5. PostgreSQL veritabanı oluşturun ve bağlantı bilgilerini settings.py dosyasında güncelleyin.

6. Migrasyonları uygulayın:

```
python manage.py migrate

```

7. Örnek veri ekleyin (isteğe bağlı):


```
python manage.py loaddata sample_data.json

```
8. Sunucuyu başlatın:

```
python manage.py runserver

```

9. Tarayıcıda http://127.0.0.1:8000/ adresine giderek uygulamayı görüntüleyin.

## Kullanım

* Ana sayfada üyelik oluşturabilir veya giriş yapabilirsiniz.
* İHA Kiralama, Kiralama İptali, Kiralama Düzenleme ve Listeleme işlemlerinizi Kiralamalarım sayfasından yapabilirsiniz.
* Kiralama işlemleri için Ana Sayfada listlenmiş ihalardan müsait olanı seçebilirsiniz.
* Filtreleme ve arama özelliklerini kullanarak verileri listeleyebilirsiniz.

## Ekstralar

* Dökümantasyon ve yorum satırları kod içinde bulunmaktadır.
* Listeleme sayfalarında datatable kullanılmıştır.
* Ön yüzde asenkron yapılar kullanılarak daha hızlı ve akıcı bir deneyim sağlanmıştır.
* İlişkisel tabloların ayrı ayrı tutulmuştur.
* Bootstrap ve jQuery gibi ön yüz kütüphaneleri kullanılmıştır.

## Katkıda Bulunma

* Projeyle ilgili herhangi bir sorunuz veya geri bildiriminiz varsa lütfen GitHub üzerinden iletişime geçin.
* Projeye katkıda bulunmak isterseniz lütfen bir pull request oluşturun.
