from rest_framework import serializers
from .models import EP, FieldEP

from rest_framework import viewsets


class EPSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EP
        fields = ('id', 'kode_ep', 'nama_ep', 'lokasi', 'google_places_id')


class FieldEPSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FieldEP
        fields = ('id', 'kode_ep', 'kode_field', 'nama_field', 'lokasi', 'google_places_id')



#ViewSet
class EPViewSet(viewsets.ModelViewSet):

    queryset = EP.objects.all()
    serializer_class = EPSerialiser


class FieldEPViewSet(viewsets.ModelViewSet):

    queryset = FieldEP.objects.all()
    serializer_class = FieldEPSerialiser
