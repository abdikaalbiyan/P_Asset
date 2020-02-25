# Generated by Django 2.2.4 on 2019-08-24 06:51

from django.db import migrations
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('EP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ep',
            name='address',
            field=django_google_maps.fields.AddressField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ep',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='fieldep',
            name='address',
            field=django_google_maps.fields.AddressField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fieldep',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
