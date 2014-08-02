from django.shortcuts import render_to_response
from restaurant.models import News


def home(request):
    actu = News.objects.all().order_by('-posted')[0]
    return render_to_response('home.html', {'current': 'home', 'actu': actu})


def contact(request):
    return render_to_response('contact.html', {'current': 'contact'})


def news(request):
    news = News.objects.all().order_by('posted')
    return render_to_response('news.html', {'current': 'news', 'news': news})

def menus(request):
    return render_to_response('menus.html', {'current': 'menus'})
