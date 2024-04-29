import os

from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название экскурсии', unique=True)
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    long_description = HTMLField(verbose_name='Полное описание', blank=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Долгота')
    lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Широта')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


def get_upload_path(instance, filename):
    return os.path.join('places', str(instance.place.id), filename)


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE,
                              related_name='images',
                              verbose_name='Название экскурсии')

    img = models.ImageField(upload_to=get_upload_path,
                            verbose_name='Изображение')

    order = models.PositiveIntegerField(default=0,
                                        blank=True,
                                        verbose_name='Номер изображения',
                                        db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order} {self.place.title}'

