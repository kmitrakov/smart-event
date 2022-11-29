from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu = [{'title': "About", 'urlname': 'about'},
        {'title': "Event Add", 'urlname': 'eventadd'},
        {'title': "Contact", 'urlname': 'contact'},
        {'title': "Sign In", 'urlname': 'signin'}
        ]


def index(request):
    events_to_show = Event.objects.all()

    context = {
        'title': 'Main Page',
        'menu': menu,
        'events_to_show': events_to_show
    }

    return render(request, 'event/index.html', context=context)


def events(request, event_id):
    event_to_show = Event.objects.filter(id=event_id)

    if len(event_to_show) == 1:
        context = {
            'title': 'Event',
            'menu': menu,
            'event_to_show': event_to_show[0]
        }

        return render(request, 'event/event.html', context=context)
    else:
        context = {
            'title': 'Event None',
            'menu': menu
        }

        return render(request, 'event/event_none.html', context=context)


def about(request):
    context = {
        'title': 'About',
        'menu': menu
    }

    return render(request, 'event/about.html', context=context)


def eventadd(request):
    context = {
        'title': 'Event Add',
        'menu': menu
    }

    return render(request, 'event/event_add.html', context=context)


def contact(request):
    context = {
        'title': 'Contact',
        'menu': menu
    }

    return render(request, 'event/event_add.html', context=context)


def signin(request):
    context = {
        'title': 'Sign In',
        'menu': menu
    }

    return render(request, 'event/signin.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена.")
