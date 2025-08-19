from http.client import responses

from django.http import HttpResponse
from django.shortcuts import render

def index(request) -> HttpResponse:
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context)

def about(request) -> HttpResponse:
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'tex_on_page': 'Lorem ipsum dolor sit amet lorem ipsum dolor sit amet ipsum dolor sit amet ipsum dolor sit amet.'
    }
    return render(request, 'main/about.html', context)

