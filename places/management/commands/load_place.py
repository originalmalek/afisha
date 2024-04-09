import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Upload place from json file'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--url', default=False, help='Url to Json file')

    def handle(self, *args, **options):
        place_json_url = options['url']
        response = requests.get(place_json_url)
        response.raise_for_status()
        place = response.json()
        new_place, created = Place.objects.get_or_create(
            title=place['title'],
            defaults={
                'short_description': place['description_short'],
                'long_description': place['description_long'],
                'lng': place['coordinates']['lng'],
                'lat': place['coordinates']['lat']
            }
        )

        if created:
            for img_url in place['imgs']:
                response = requests.get(img_url)
                if response.ok:
                    img_data = response.content
                    img_name = img_url.split("/")[-1]
                    Image.objects.create(place = new_place, img=ContentFile(img_data, name=img_name))

        else:
            print("Place wasn't added because it already exists")