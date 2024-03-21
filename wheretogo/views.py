import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from places.models import Place, Image


def generate_place_json(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = Image.objects.filter(place=place)

    imgs = [image.img.url for image in images]

    response = {
    'title': place.title,
    'imgs': imgs,
    'description_short': place.description_short,
    'description_long': place.description_long,
    'coordinates': {
        'lng': str(place.lng),
        'lat': str(place.lat)
    }}

    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')

def index_page(request):
    places = Place.objects.all()
    places_list = []

    for place in places:
        places_list.append({
          'type': 'Feature',
          'geometry': {
            'type': 'Point',
            'coordinates': [place.lng, place.lat]
          },
          'properties': {
            'title': place.title,
            'placeId': place.id,
            'detailsUrl': f'/place/{place.id}'
          }
        })

    return render(request, 'places/templates/index.html', {'places': json.dumps(places_list)})
