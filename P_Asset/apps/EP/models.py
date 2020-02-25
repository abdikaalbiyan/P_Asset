from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone

from django_google_maps import fields as map_fields

import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class EP(models.Model):
    kode_ep = models.CharField(blank=True, max_length=100)
    nama_ep = models.CharField(blank=True, max_length=100)
    lokasi = models.CharField(blank=True, max_length=100)
    google_places_id = models.CharField(max_length=255, blank=True)

    address = map_fields.AddressField(max_length=200, blank=True, null=True, default=None)
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.kode_ep


class FieldEP(models.Model):
    kode_ep = models.ForeignKey(EP, on_delete=models.CASCADE)
    kode_field = models.CharField(blank=True, max_length=100)
    nama_field = models.CharField(blank=True, max_length=100)
    lokasi = models.CharField(blank=True, max_length=100)
    google_places_id = models.CharField(max_length=255, blank=True)

    address = map_fields.AddressField(max_length=200, blank=True, null=True, default=None)
    geolocation = map_fields.GeoLocationField(max_length=100, blank=True, null=True, default=None)

    def __str__(self):
        return self.kode_field
