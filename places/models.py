from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название экскурсии')
    short_description = models.TextField(verbose_name='Краткое описание', blank=True, null=True)
    long_description = HTMLField(verbose_name='Полное описание', blank=True, null=True)
    lng = models.CharField(max_length=20, verbose_name='Долгота')
    lat = models.CharField(max_length=20, verbose_name='Широта')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


def get_upload_path(instance, filename):
    return f'places/{instance.place.id}/{filename}'


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    img = models.ImageField(upload_to=get_upload_path)
    order = models.PositiveIntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order} {self.place.title}'

