from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime

from django_google_maps import fields as map_fields

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

from P_Asset.apps.EP.models import FieldEP
from P_Asset.apps.users.models import CustomUser


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Asset(models.Model):
    kode_field = models.ForeignKey(FieldEP, on_delete=models.CASCADE, default=None)
    kode_asset = models.CharField(blank=True, max_length=100)
    nama = models.CharField(blank=True, max_length=100)
    merk = models.CharField(blank=True, max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tahun_pembuatan = models.PositiveIntegerField(
                                default=current_year(),
                                validators=[MinValueValidator(1970),
                                max_value_current_year])
    umur_asset = models.FloatField(blank=True, max_length=100)
    harga = models.FloatField(blank=True, null=True)
    tgl_beli = models.DateTimeField(blank=True, null=True)
    lokasi = models.CharField(blank=True, max_length=100)
    deskripsi = models.TextField(blank=True)
    foto = models.ImageField(blank=True)
    surat_kepemilikan = models.TextField(blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    google_places_id = models.CharField(max_length=255, blank=True)

    jenis_sewa = models.CharField(max_length=1)

    address = map_fields.AddressField(max_length=200, blank=True, null=True, default=None)
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return f"[{self.kode_asset}, {self.nama}]"


class AssetMasyarakat(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    kode_asset = models.CharField(blank=True, max_length=100)
    nama = models.CharField(blank=True, max_length=100)
    merk = models.CharField(blank=True, max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tahun_pembuatan = models.PositiveIntegerField(
                                default=current_year(),
                                validators=[MinValueValidator(1970),
                                max_value_current_year])
    umur_asset = models.CharField(blank=True, max_length=100)
    harga = models.FloatField(blank=True, null=True)
    tgl_beli = models.DateTimeField(blank=True, null=True)
    lokasi = models.CharField(blank=True, max_length=100)
    deskripsi = models.TextField(blank=True)
    foto = models.ImageField(blank=True)
    surat_kepemilikan = models.TextField(blank=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    google_places_id = models.CharField(max_length=255, blank=True)

    address = map_fields.AddressField(max_length=200, blank=True, null=True, default=None)
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return f"[{self.kode_asset}, {self.nama}]"
