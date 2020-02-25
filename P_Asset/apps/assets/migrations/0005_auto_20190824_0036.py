# Generated by Django 2.2.4 on 2019-08-23 17:36

import P_Asset.apps.assets.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20190824_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='tahun_pembuatan',
            field=models.PositiveIntegerField(default=2019, validators=[django.core.validators.MinValueValidator(1970), P_Asset.apps.assets.models.max_value_current_year]),
        ),
        migrations.AlterField(
            model_name='assetmasyarakat',
            name='tahun_pembuatan',
            field=models.PositiveIntegerField(default=2019, validators=[django.core.validators.MinValueValidator(1970), P_Asset.apps.assets.models.max_value_current_year]),
        ),
    ]