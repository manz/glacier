from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.views.decorators.http import require_http_methods
from restaurant.forms import EventForm
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
    events = Event.objects.all().order_by('-posted')
    return render_to_response('news.html', {'current': 'news', 'events': events})


def menus(request):
    return render_to_response('menus.html', {'current': 'menus'})


@login_required
@require_http_methods(['GET', 'POST'])
def edit_event(request, event_id=None):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            if event_id is not None:
                event = Event.objects.get(pk=event_id)
            else:
                event = Event()
            event.title = form.cleaned_data['title']
            event.content = form.cleaned_data['content']
            event.posted = form.cleaned_data['posted']
            event.save()
            return redirect('news')
    elif request.method == 'GET':
        if event_id is not None:
            event = Event.objects.get(pk=event_id)
            form = EventForm({
                'title': event.title,
                'posted': event.posted,
                'content': event.content
            })
        else:
            form = EventForm()

    return render_to_response('edit_event.html', {'event_form': form},
                                  context_instance=RequestContext(request))

