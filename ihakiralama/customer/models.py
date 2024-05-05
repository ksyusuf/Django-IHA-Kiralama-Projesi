from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):
    Customer_id = models.AutoField(primary_key=True)
    Ad = models.CharField(max_length=200)
    Soyad = models.CharField(max_length=200)
    Mail = models.EmailField()
    GsmNo = models.CharField(max_length=15)
    Sifre = models.CharField(max_length=20)
    Status = models.BooleanField(default=True)


class Ihas(models.Model):
    Iha_id = models.AutoField(primary_key=True)
    Marka = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Agirlik = models.FloatField()
    Kategori = models.CharField(max_length=100)
    Kanat_w = models.FloatField()  # kanat genişliği
    Adet = models.IntegerField()
    Musaitlik = models.IntegerField()
    Bakim_yapildi_mi = models.BooleanField(default=True)
    Status = models.BooleanField(default=True)


class Category(models.Model):
    Category_id = models.AutoField(primary_key=True)
    ModelName = models.CharField(max_length=100)
    Status = models.BooleanField(default=True)


class Rent(models.Model):
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Iha_id = models.ForeignKey(Ihas, on_delete=models.CASCADE)
    kira_baslangic = models.DateTimeField(default=timezone.now)
    kira_bitis = models.DateTimeField(null=True, blank=True)
