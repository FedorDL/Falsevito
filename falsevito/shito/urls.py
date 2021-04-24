from django.conf.urls import url
from .views import index
from .views import secure


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'secure', secure, name='secure')
]