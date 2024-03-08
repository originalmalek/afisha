import json

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from places.models import Place


def first_page(request):
    places = Place.objects.all()
    places_list = []
    for place in places:
        places_list.append({
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
          }
        })

    return render(request, 'where/index.html', {'places': json.dumps(places_list)})
