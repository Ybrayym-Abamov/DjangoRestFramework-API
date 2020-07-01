from django.conf.urls import url, include

from api.views import ManufacturerViewSet, ShoeColorViewSet, ShoeTypeViewSet, ShoesViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'manufacturer', ManufacturerViewSet)
router.register(r'shoe-color', ShoeColorViewSet)
router.register(r'shoe-type', ShoeTypeViewSet)
router.register(r'shoe', ShoesViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]
