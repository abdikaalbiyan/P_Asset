from rest_framework import serializers
from .models import CustomUser

from rest_framework import viewsets
from django.conf import settings


class CustomUserSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')


#ViewSet
class CustomUserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerialiser
