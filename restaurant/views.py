from django.shortcuts import render_to_response
from restaurant.models import Event


def home(request):
    try:
        event = Event.objects.all().order_by('-posted')[0]
    except IndexError:
        event = None
    return render_to_response('home.html', {'current': 'home', 'event': event})


def contact(request):
    return render_to_response('contact.html', {'current': 'contact'})


def news(request):
    events = Event.objects.all().order_by('posted')
    return render_to_response('news.html', {'current': 'news', 'event': events})


def menus(request):
    return render_to_response('menus.html', {'current': 'menus'})
