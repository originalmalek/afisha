import json
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'wheretogo.settings'
import django
django.setup()

from places.models import Place

def store_json_to_db(json_data):
    new_place = Place(title=json_data['title'],
                      description_short=json_data['description_short'],
                      description_long=json_data['description_long'],
                      lng=json_data['coordinates']['lng'],
                      lat=json_data['coordinates']['lat'])


    new_place.save()

def save_json_files_to_db(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            with open(os.path.join(directory_path, filename), 'r') as f:
                json_data = json.load(f)

        store_json_to_db(json_data)


save_json_files_to_db('places')