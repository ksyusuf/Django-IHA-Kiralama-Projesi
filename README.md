# İHA Kiralama Projesi  →  [Fotoğraf Albümü](#fotoğraf-albümü)


Bu proje, Django ve PostgreSQL kullanılarak geliştirilen bir İnsansız Hava Aracı (İHA) kiralama web uygulamasıdır.
Projede, üyelik sistemi ve kiralama işlemleri yapılabilmektedir.

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

# Fotoğraf Albümü

Bu repo, içerisinde bir fotoğraf albümü bulunduruyor. Aşağıda albümde yer alan fotoğrafların listesi ve dosya isimleri bulunmaktadır:

## Ana Sayfa (ziyaretçi)

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Ana%20Sayfa%20(ziyaret%C3%A7i).png" alt="Ana Sayfa (giriş yapılmış)" width="700">

## Ana Sayfa (giriş yapılmış)

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Ana%20Sayfa%20(giri%C5%9F%20yap%C4%B1lm%C4%B1%C5%9F).png" alt="Ana Sayfa (giriş yapılmış)" width="700">

## Detaylar (kiralamaya başla)

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Detaylar.png" alt="Detaylar" width="700">

## Kiralama Tarihleri

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kiralama%20Tarihleri.png" alt="Kiralama Tarihleri" width="700">

## Kiralama Tarihleri (tarih seçimi)

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kiralama%20Tarihleri%20(tarih%20se%C3%A7imi).png" alt="Kiralama Tarihleri (tarih seçimi)" width="700">

## Kiralama Tarihleri (bakımsız iha kiralama)

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kiralama%20Tarihleri%20(bak%C4%B1ms%C4%B1z%20iha%20kiralama).png" alt="Kiralama Tarihleri (bakımsız iha kiralama)" width="700">

## Kiralamalarım (iyi sürüşler)

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kiralamalar%C4%B1m%20(iyi%20s%C3%BCr%C3%BC%C5%9Fler).png" alt="Kiralamalarım" width="700">

## Kiralamalarım

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kiralamalar%C4%B1m.png" alt="Kiralamalarım" width="700">

## Kiralama Düzenle

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kiralama%20D%C3%BCzenle.png" alt="Kiralama Düzenle" width="700">

## Kiralamalarım (düzenleme)

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kiralamalar%C4%B1m%20(d%C3%BCzenleme).png" alt="Kiralamalarım (düzenleme)" width="700">

## Kullanıcı Kayıt

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kullan%C4%B1c%C4%B1%20Kay%C4%B1t.png" alt="Kullanıcı Kayıt" width="700">

## Kullanıcı Kayıt (mail zaten var)

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kullan%C4%B1c%C4%B1%20Kay%C4%B1t%20(mail%20zaten%20var).png" alt="Kullanıcı Kayıt (mail zaten var)" width="700">

## Kullanıcı Kayıt (şifreler eşleşmiyor)

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kullan%C4%B1c%C4%B1%20Kay%C4%B1t%20(%C5%9Fifreler%20e%C5%9Fle%C5%9Fmiyor).png" alt="Kullanıcı Kayıt (şifreler eşleşmiyor)" width="700">

## Kullanıcı Giriş

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kullan%C4%B1c%C4%B1%20Giri%C5%9F.png" alt="Kullanıcı Giriş" width="700">

## Kullanıcı Giriş (şifre yanlış)

<img src="https://github.com/ksyusuf/Django-IHA-Kiralama-Projesi/blob/master/Ekran%20g%C3%B6r%C3%BCnt%C3%BCleri/IHA%20-%20Kullan%C4%B1c%C4%B1%20Giri%C5%9F%20(%C5%9Fifre%20yanl%C4%B1%C5%9F).png" alt="Kullanıcı Giriş (şifre yanlış)" width="700">

[Başa Dön](#i%CC%87ha-kiralama-projesi----foto%C4%9Fraf-alb%C3%BCm%C3%BC)
