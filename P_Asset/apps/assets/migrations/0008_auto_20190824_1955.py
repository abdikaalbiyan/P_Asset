# Generated by Django 2.2.4 on 2019-08-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_asset_jenis_sewa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='jenis_sewa',
            field=models.CharField(max_length=1),
        ),
    ]
