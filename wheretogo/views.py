import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from places.models import Place, Image


def generate_place_json(request, place_id):
    imgs =[]
    place = get_object_or_404(Place, pk=place_id)
    images = Image.objects.filter(place=place)
    for image in images:
        imgs.append(image.img.url)
    response = {
    "title": place.title,
    "imgs": imgs,
    "description_short": place.description_short,
    "description_long": place.description_long,
    "coordinates": {
        "lng": str(place.lng),
        "lat": str(place.lat)
    }}

    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type="application/json")

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
            "detailsUrl": f"http://127.0.0.1:8000/place/{place.id}"
          }
        })

    return render(request, 'where/index.html', {'places': json.dumps(places_list)})
