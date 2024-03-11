from django.utils.html import format_html
from django.contrib import admin
from .models import Place, Image

class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.img:  # Обновляем здесь на `img`
            return format_html('<img src="{}" height="200" />', obj.img.url)  # И здесь на `img`
        else:
            return "No Image Found"
    image_preview.short_description = 'Image Preview'

class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Place, PlaceAdmin)