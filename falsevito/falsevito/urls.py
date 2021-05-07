from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from falsevito import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shito.urls'))
]

#STATIC_URLS
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#MEDIA_URLS
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

