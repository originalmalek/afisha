import json

from django.db.models import Prefetch
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place, Image


def generate_place_json(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related(Prefetch("images")), pk=place_id)

    imgs = [image.img.url for image in place.images.all()]

    response = {
        'title': place.title,
        'imgs': imgs,
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': str(place.lng),
            'lat': str(place.lat)
        }}

    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def index_page(request):
    places = Place.objects.all()
    on_map_places = []

    for place in places:
        on_map_places.append({
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse(generate_place_json, args=[place.id])
            }
        })
    print(reverse(generate_place_json, args=[place.id]))
    return render(request, template_name='places/templates/places/index.html',
                  context={'places': {"type": "FeatureCollection",
                                      "features": on_map_places}})
