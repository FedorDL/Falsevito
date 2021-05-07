from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'shito'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'secure/', views.secure, name='secure'),
    path('ad/all/', views.ad_all, name='ad_all'),
    path('category/', views.category, name='category'),
    path('favorites/', views.favorites, name='favorites'),
    path('ad/create/', views.ad_create, name='ad_create'),
    path('ad/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('ad/<int:ad_id>/edit/', views.ad_edit, name='ad_edit'),
    path('ad/<int:ad_id>/delete/', views.ad_delete, name='ad_delete'),
    path('ad/<int:ad_id>/like/', views.like_ad, name='like_ad')
]

