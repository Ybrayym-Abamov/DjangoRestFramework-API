from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import HyperlinkedModelSerializer

from shoes.models import Manufacturer, ShoeColor, ShoeType, Shoes


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'website')


class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('id', 'style',)


class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('id', 'color_name',)


class ShoesSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoes
        fields = ('size', 'brand', 'name', 'manufacturer', 'color', 'material',
                  'shoe_type', 'fasten_type')
