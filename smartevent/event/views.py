from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *


def index(request):
    events_to_show = Event.objects.all()
    return render(request, 'event/index.html', {'events_to_show': events_to_show, 'title': 'Main Page'})


def events(request, event_id):
    event_to_show = Event.objects.filter(id=event_id)

    if len(event_to_show) == 1:
        return render(request, 'event/event.html', {'event_to_show': event_to_show[0], 'title': 'Event'})
    else:
        return render(request, 'event/event_none.html', {'title': 'Event None'})


def about(request):
    return render(request, 'event/about.html', {'title': 'About'})


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена.")
