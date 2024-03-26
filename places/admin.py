from django.contrib import admin
from .models import Image, Place
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin

IMAGE_WIDTH = 200

@admin.register(Image)
class AdminImage(admin.ModelAdmin, SortableAdminMixin):
    readonly_fields = ['get_preview']
    def get_preview(self, obj):
        return mark_safe('<img src="{url}" height=200 />'.format(
            url=obj.img.url, ))


class AdminImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    list_display = ('image', 'get_preview',)
    readonly_fields = ['get_preview']
    extra = 0
    def get_preview(self, obj):
        return mark_safe('<img src="{url}" width={width} />'.format(
            url=obj.img.url,
            width=IMAGE_WIDTH, ))

@admin.register(Place)
class AdminPlace(SortableAdminMixin, admin.ModelAdmin):
    inlines = [AdminImageInline]