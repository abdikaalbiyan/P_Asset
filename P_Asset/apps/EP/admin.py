# users/admin.py
from django.contrib import admin

from .models import EP, FieldEP


class EPAdmin(admin.ModelAdmin):
    search_fields = ('kode_ep', 'nama_ep')
    list_display = ('kode_ep', 'nama_ep')


class FieldEPAdmin(admin.ModelAdmin):
    search_fields = ('kode_field', 'nama_field')
    list_display = ('kode_field', 'nama_field')


admin.site.register(EP, EPAdmin)
admin.site.register(FieldEP, FieldEPAdmin)
