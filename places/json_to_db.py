import json
import os
import sys
from pathlib import Path

import django
import requests
from django.core.files.base import ContentFile

path = Path(__file__).resolve()

sys.path.append(str(path.parent.parent))
os.environ['DJANGO_SETTINGS_MODULE'] = 'wheretogo.settings'

django.setup()

from places.models import Place, Image


def store_json_to_db(json_data):
    new_place = Place(title=json_data['title'],
                      short_description=json_data['description_short'],
                      long_description=json_data['description_long'],
                      lng=json_data['coordinates']['lng'],
                      lat=json_data['coordinates']['lat'])

    new_place.save()

    for img_url in json_data['imgs']:
        response = requests.get(img_url)

        if response.status_code == 200:
            img_data = response.content
            img_name = img_url.split("/")[-1]

            new_image = Image(place=new_place)
            new_image.img.save(img_name, ContentFile(img_data), save=True)


def save_json_files_to_db(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            with open(os.path.join(directory_path, filename), 'r') as f:
                json_data = json.load(f)

        store_json_to_db(json_data)


save_json_files_to_db('content')
print('The content succesfully uploaded')
