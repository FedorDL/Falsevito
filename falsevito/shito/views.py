from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Salam Bratuha!')


def secure(request):
    return HttpResponse('You from sberbank?')
