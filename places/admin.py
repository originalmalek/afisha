from django.contrib import admin
from .models import Image, Place
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.utils.html import format_html


IMAGE_WIDTH = 200

@admin.register(Image)
class AdminImage(admin.ModelAdmin, SortableAdminMixin):
    readonly_fields = ['get_preview']
    autocomplete_fields = ['place']
    def get_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px; max-width: 200px"/>', obj.img.url)


class AdminImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    list_display = ('image', 'get_preview',)
    readonly_fields = ['get_preview']
    extra = 0

    def get_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px; max-width: 200px"/>', obj.img.url)

@admin.register(Place)
class AdminPlace(SortableAdminMixin, admin.ModelAdmin):
    inlines = [AdminImageInline]
    search_fields = ['title', ]