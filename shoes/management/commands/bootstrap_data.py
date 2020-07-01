from django.core.management.base import BaseCommand

from shoes.models import ShoeType, ShoeColor


class Command(BaseCommand):
    def handle(self, *args, **options):
        shoe_type = [
            'sneaker',
            'boot',
            'sandal',
            'dress',
            'other'
        ]
        shoe_color = [
            'RED',
            'ORANGE',
            'GREEN',
            'BLUE',
            'INDIGO',
            'VIOLET',
            'WHITE',
            'BLACK'
        ]
        for type in shoe_type:
            ShoeType.objects.create(style=type)
        for color in shoe_color:
            ShoeColor.objects.create(color_name=color)
