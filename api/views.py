from rest_framework.viewsets import ModelViewSet
from api import serializers
from shoes import models


class ManufacturerViewSet(ModelViewSet):
    serializer_class = serializers.ManufacturerSerializer
    queryset = models.Manufacturer.objects.all()


class ShoeTypeViewSet(ModelViewSet):
    serializer_class = serializers.ShoeTypeSerializer
    queryset = models.ShoeType.objects.all()


class ShoeColorViewSet(ModelViewSet):
    serializer_class = serializers.ShoeColorSerializer
    queryset = models.ShoeColor.objects.all()


class ShoesViewSet(ModelViewSet):
    serializer_class = serializers.ShoesSerializer
    queryset = models.Shoes.objects.all()
