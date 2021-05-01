from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile, Ad, Category


def secure(request):
    return HttpResponse('You from sberbank?')


def index(request):
    ad_queryset = Ad.objects.all().order_by('-date_pub')[:7]

    return HttpResponse(ad_queryset)


def ad_all(request):
    ad_queryset = Ad.objects.all()
    return HttpResponse(ad_queryset)


def ad_edit(request, ad_id):
    return HttpResponse(f'Редактирование объявления - {ad_id}')


def ad_create(request):
    return HttpResponse(f'Создание объявления')


def ad_delete(request, ad_id):
    return HttpResponse(f'Удаление объявления - {ad_id}')


def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return HttpResponse(f'Детальное описание объявления - {ad_id}, Название - {ad.title} / описание - {ad.descpition}')


def like_ad(request, ad_id):
    return HttpResponse(f'Добавить в избранное - объявление {ad_id}')


def category(request):
    return HttpResponse(f'Объявления по категориям')


def favorites(request):
    user = request.user
    profile_queryset = Profile.objects.filter(user__in = user.user_profile.favorites.all())
    output = ['id:{} // \n'.format(user.id) for u in profile_queryset]
    return HttpResponse(output)


