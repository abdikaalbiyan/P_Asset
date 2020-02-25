from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from django.urls import include, path

from . import users_api


router = routers.DefaultRouter()
router.register(r'CustomUser', users_api.CustomUserViewSet)

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        path('', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
