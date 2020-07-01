from django.conf.urls import url, include

from api.views import ManufacturerViewSet, ShoeColorViewSet, ShoeTypeViewSet, ShoesViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'shoe-colors', ShoeColorViewSet)
router.register(r'shoe-types', ShoeTypeViewSet)
router.register(r'shoes', ShoesViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]
