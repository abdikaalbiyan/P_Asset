# Generated by Django 2.2.4 on 2019-08-23 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_ep', models.CharField(blank=True, max_length=100)),
                ('nama_ep', models.CharField(blank=True, max_length=100)),
                ('lokasi', models.CharField(blank=True, max_length=100)),
                ('google_places_id', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FieldEP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_field', models.CharField(blank=True, max_length=100)),
                ('nama_field', models.CharField(blank=True, max_length=100)),
                ('lokasi', models.CharField(blank=True, max_length=100)),
                ('google_places_id', models.CharField(blank=True, max_length=255)),
                ('kode_ep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EP.EP')),
            ],
        ),
    ]
