from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=30)

    def __str__(self):
        return self.style


# https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
class ShoeColor(models.Model):
    RED = 'R'
    ORANGE = 'O'
    GREEN = 'G'
    BLUE = 'B'
    INDIGO = 'I'
    VIOLET = 'V'
    WHITE = 'W'
    BLACK = 'B'
    COLOR_CHOICES = [
        (RED, 'Red'),
        (ORANGE, 'Orange'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black')
    ]
    color_name = models.CharField(max_length=10, choices=COLOR_CHOICES,
                                  default=BLACK)

    def __str__(self):
        return self.color_name


class Shoes(models.Model):
    size = models.IntegerField(default=7)
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=30)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=30)

    def __str__(self):
        return self.name
