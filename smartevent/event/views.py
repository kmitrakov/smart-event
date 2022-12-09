from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView

from .forms import *
from .models import *

# TODO: Необходимо отрефакторить метод отрисовки menu_main в шаблоне base.html.
#  Избавиться от дублирования кода.
menu_main = [{'title': "Main Page", 'urlname': 'index'},
             {'title': "Event Add", 'urlname': 'event_add'},
             {'title': "Contact", 'urlname': 'contact'},
             {'title': "About", 'urlname': 'about'},
             {'title': "Sign Out", 'urlname': 'sign_out'},
             {'title': "Sign In", 'urlname': 'sign_in'},
             {'title': "My Space", 'urlname': 'my_space'}
             ]


class EventIndex(ListView):
    model = Event
    template_name = 'event/index.html'
    context_object_name = 'events'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main Page'
        context['menu_main'] = menu_main
        return context

    def get_queryset(self):
        return Event.objects.filter(scope=1)


class EventShow(DetailView):
    model = Event
    template_name = 'event/event.html'
    pk_url_kwarg = 'event_id'
    context_object_name = 'event'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Event'
        context['menu_main'] = menu_main
        return context


def about(request):
    context = {
        'title': 'About',
        'menu_main': menu_main
    }

    return render(request, 'event/about.html', context=context)


def event_add(request):
    if request.method == 'POST':
        form = EventAddForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('index')
    else:
        form = EventAddForm()

    context = {
        'title': 'Event Add',
        'menu_main': menu_main,
        'form': form
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


def my_space(request):
    context = {
        'title': 'My Space',
        'menu_main': menu_main
    }

    return render(request, 'event/my_space.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена.")
