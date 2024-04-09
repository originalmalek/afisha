from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from places.views import index_page, generate_place_json

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index_page),
                  path('place/<int:place_id>/', generate_place_json, name='generate-place-json'),
                  path('tinymce/', include('tinymce.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()