from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

menu_main = [{'title': "Sign In", 'urlname': 'sign_in'},
             {'title': "Sign Out", 'urlname': 'sign_out'},
             {'title': "Event Add", 'urlname': 'event_add'},
             {'title': "Main Page", 'urlname': 'index'},
             {'title': "Contact", 'urlname': 'contact'},
             {'title': "About", 'urlname': 'about'}
             ]


def index(request):
    events_to_show = Event.objects.filter(scope=1)

    context = {
        'title': 'Main Page',
        'menu_main': menu_main,
        'events_to_show': events_to_show
    }

    return render(request, 'event/index.html', context=context)


def events(request, event_id):
    event_to_show = Event.objects.filter(id=event_id)

    if len(event_to_show) == 1:
        context = {
            'title': 'Event',
            'menu_main': menu_main,
            'event_to_show': event_to_show[0]
        }

        return render(request, 'event/event.html', context=context)
    else:
        context = {
            'title': 'Event None',
            'menu_main': menu_main,
        }

        return render(request, 'event/event_none.html', context=context)


def about(request):
    context = {
        'title': 'About',
        'menu_main': menu_main
    }

    return render(request, 'event/about.html', context=context)


def event_add(request):
    context = {
        'title': 'Event Add',
        'menu_main': menu_main
    }

    return render(request, 'event/event_add.html', context=context)


def contact(request):
    context = {
        'title': 'Contact',
        'menu_main': menu_main
    }

    return render(request, 'event/contact.html', context=context)


def sign_in(request):
    context = {
        'title': 'Sign In',
        'menu_main': menu_main
    }

    return render(request, 'event/sign_in.html', context=context)

def sign_out(request):
    context = {
        'title': 'Sign Out',
        'menu_main': menu_main
    }

    return render(request, 'event/sign_out.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена.")
