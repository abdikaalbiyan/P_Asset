from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from . import assets_api
from django.urls import include, path


router = routers.DefaultRouter()
router.register(r'Category', assets_api.CategoryViewSet)
router.register(r'Asset', assets_api.AssetViewSet)
router.register(r'AssetMasyarakat', assets_api.AssetMasyarakatViewSet)

urlpatterns = [
        url(r'^admin/', admin.site.urls),
        path('', include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
