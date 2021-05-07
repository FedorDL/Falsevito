from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Profile, Ad, Category
from .forms import AdForm


def secure(request):
    return HttpResponse('You from sberbank?')


def index(request):
    ad_queryset = Ad.objects.all().order_by('-date_pub')[:7]

    return render(request, 'shito/index.html', {'index_ads': ad_queryset})


def ad_all(request):
    ad_queryset = Ad.objects.all()

    return render(request, 'shito/ad_all.html', {'ad_all': ad_queryset})


def ad_edit(request, ad_id):
    return HttpResponse(f'Редактирование объявления - {ad_id}')


def ad_create(request):
    template_name = 'shito/ad_create.html'
    context = {'form': AdForm()}

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            context['ad_was_created'] = True
        else:
            context['ad_with_errors'] = True
            context['form'] = form
    return render(request, template_name, context)


def ad_delete(request, ad_id):
    return HttpResponse(f'Удаление объявления - {ad_id}')


def ad_detail(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    return render(request, 'shito/ad_detail.html', {'ad': ad})


def like_ad(request, ad_id):
    profile = get_object_or_404(Ad, id=ad_id)
    if request.user in Profile.favorites.all():
        Profile.favorites.remove(request.user)
    else:
        Profile.favorites.add(request.user)
        profile.save()
    return redirect(request.META.get('HTTP_REFERER'), request)


def category(request):
    ad_queryset = Ad.objects.all()
    category_queryset = Category.objects.all()
    return render(request, 'shito/category.html', {'category': category_queryset})


def favorites(request):
    user = request.user
    profile_queryset = Profile.objects.filter(user__in = user.user_profile.favorites.all())
    output = ['id:{} // \n'.format(user.id) for u in profile_queryset]
    return HttpResponse(output)


