from django.db import models



class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название экскурсии')
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)

    def __str__(self):
        return self.title



class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media')
    order = models.PositiveIntegerField(default=0)


    class Meta:
        unique_together = ('place', 'order')
    def __str__(self):
        return f'{self.order} {self.place.title}'

    def save(self, *args, **kwargs):
        if not self.order:  # if order is not set
            max_order = Image.objects.filter(place=self.place).aggregate(models.Max('order'))['order__max'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)