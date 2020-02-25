# users/admin.py
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

from .models import Category, Asset, AssetMasyarakat


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('id', 'category_name')
    list_display = ('id', 'category_name')


class AssetAdmin(admin.ModelAdmin):
    search_fields = ('nama', 'kode_asset')
    list_display = ('kode_asset', 'nama', 'category', 'harga')
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }


class AssetMasyarakatAdmin(admin.ModelAdmin):
    search_fields = ('nama', 'kode_asset')
    list_display = ('kode_asset', 'nama', 'owner', 'category', 'harga')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(AssetMasyarakat, AssetMasyarakatAdmin)
