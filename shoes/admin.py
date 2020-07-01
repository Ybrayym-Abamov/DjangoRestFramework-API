from django.contrib import admin
from shoes.models import Manufacturer, ShoeColor, ShoeType, Shoes

admin.site.register(Manufacturer)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)
admin.site.register(Shoes)
