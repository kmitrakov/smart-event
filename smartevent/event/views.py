from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class EventIndex(DataMixin, ListView):
    model = Event
    template_name = 'event/index.html'
    context_object_name = 'events'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Main Page')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Event.objects.filter(scope=1)


class EventShow(DataMixin, DetailView):
    model = Event
    template_name = 'event/event.html'
    pk_url_kwarg = 'event_id'
    context_object_name = 'event'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Event')
        return dict(list(context.items()) + list(c_def.items()))


class EventAdd(LoginRequiredMixin, DataMixin, CreateView):
    form_class = EventAddForm
    template_name = 'event/event_add.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('sign_in')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Event Add')
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    context = {
        'title': 'About',
        'menu_main': menu_main
    }

    return render(request, 'event/about.html', context=context)


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


@login_required
def my_space(request):
    context = {
        'title': 'My Space',
        'menu_main': menu_main
    }

    return render(request, 'event/my_space.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена.")
