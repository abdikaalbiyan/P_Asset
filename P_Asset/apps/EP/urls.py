from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from . import ep_api
from django.urls import include, path


router = routers.DefaultRouter()
router.register(r'EP', ep_api.EPViewSet)
router.register(r'FieldEP', ep_api.FieldEPViewSet)

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        path('', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
