from django.db import models



class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название экскурсии')
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    lng = models.CharField(max_length=20, verbose_name='Долгота')
    lat = models.CharField(max_length=20, verbose_name='Широта')


    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title



class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media')
    order = models.PositiveIntegerField(default=0)


    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order} {self.place.title}'

    def save(self, *args, **kwargs):
        if self.order is None or Image.objects.filter(place=self.place, order=self.order).exists():
            max_order = Image.objects.filter(place=self.place).aggregate(models.Max('order'))['order__max'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)