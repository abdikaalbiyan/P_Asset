import django_filters.rest_framework
from .models import Asset, Category, AssetMasyarakat

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework import viewsets

from django.conf import settings

settings.HOST = '10.50.0.59:8080'


class AssetSerialiser(serializers.HyperlinkedModelSerializer):

    penyusutan_pertahun = serializers.SerializerMethodField()
    total_susut = serializers.SerializerMethodField()
    nilai_buku = serializers.SerializerMethodField()

    class Meta:
        model = Asset
        fields = ('id', 'kode_field', 'kode_asset', 'nama', 'merk',
                  'category', 'jenis_sewa', 'tahun_pembuatan', 'umur_asset', 'harga',
                  'tgl_beli', 'lokasi', 'deskripsi', 'foto', 'surat_kepemilikan',
                  'latitude', 'longitude', 'google_places_id', 'penyusutan_pertahun', 'total_susut', 'nilai_buku')

    def get_penyusutan_pertahun(self, obj):
        return (int(obj.harga) / int(obj.umur_asset)) if obj.harga and obj.umur_asset else 'None'

    def get_total_susut(self, obj):
        return (int(obj.harga) / int(obj.umur_asset)) * (int(2019) - int(obj.tgl_beli.year)) if obj.harga and obj.umur_asset and obj.tgl_beli else 'None'

    def get_nilai_buku(self, obj):
        return ((obj.harga - ((obj.harga / obj.umur_asset) * (float(2019 - float(obj.tgl_beli.year))))) if obj.harga and obj.umur_asset and obj.tgl_beli else 'None') if \
        ((obj.harga - (obj.harga / obj.umur_asset) * (float(2019 - float(obj.tgl_beli.year)))) if obj.harga and obj.umur_asset and obj.tgl_beli else 'None') >= 0 else 0


class AssetMasyarakatSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AssetMasyarakat
        fields = ('id', 'owner', 'kode_asset', 'nama', 'merk', 'category',
                  'tahun_pembuatan', 'umur_asset', 'harga', 'tgl_beli', 'lokasi',
                  'deskripsi', 'foto', 'surat_kepemilikan', 'latitude',
                  'longitude', 'google_places_id')


class CategorySerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name')


#ViewSet
class AssetViewSet(viewsets.ModelViewSet):

    queryset = Asset.objects.all()
    serializer_class = AssetSerialiser
    #
    # def assets_detail(request, pk):
    #     """
    #     Retrieve, update or delete a code snippet.
    #     """
    #     try:
    #         queryset = Asset.objects.get(name=name)
    #     except Asset.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #
    #     if request.method == 'GET':
    #         serializer = AssetSerialiser(queryset)
    #         return Response(serializer.data)
    #
    #     elif request.method == 'PUT':
    #         serializer = AssetSerialiser(queryset, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #     elif request.method == 'DELETE':
    #         queryset.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)


class AssetMasyarakatViewSet(viewsets.ModelViewSet):

    queryset = AssetMasyarakat.objects.all()
    serializer_class = AssetMasyarakatSerialiser


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerialiser
