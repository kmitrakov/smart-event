from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth import login

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
    model = Event
    form_class = EventAddForm
    template_name = 'event/event_add.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('sign_in')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Event Add')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.instance.user_create = self.request.user
        return super().form_valid(form)

        # form.instance.user_create = self.request.user.id
        # return super().form_valid(form)

        # self.object = form.save(commit=False)
        # self.object.user_create = self.request.user.id
        # self.object.save()
        # return HttpResponseRedirect(self.get_success_url())


class Contact(DataMixin, TemplateView):
    template_name = 'event/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Contact')
        return dict(list(context.items()) + list(c_def.items()))


class About(DataMixin, TemplateView):
    template_name = 'event/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='About')
        return dict(list(context.items()) + list(c_def.items()))


class SignOut(View):
    def get(self, request):
        logout(request)
        return redirect('index')

    # TODO: Подумать, как вернуть этот класс к типу TemplateView.


class SignUp(DataMixin, CreateView):
    form_class = SignUpForm
    template_name = 'event/sign_up.html'
    success_url = reverse_lazy('sign_in')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign Up')
        return dict(list(context.items()) + list(c_def.items()))

    # Если пользователь успешно зарегистрирован,
    # то он автоматически аутентифицируется и перенеправляется
    # на главную страницу.
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class SignIn(DataMixin, LoginView):
    form_class = SignInForm
    template_name = 'event/sign_in.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Sign In')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


class MySpace(DataMixin, TemplateView):
    template_name = 'event/my_space.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='My Space')
        return dict(list(context.items()) + list(c_def.items()))


class ForgotPassword(DataMixin, TemplateView):
    template_name = 'event/forgot_password.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Forgot Password')
        return dict(list(context.items()) + list(c_def.items()))


class Profile(DataMixin, TemplateView):
    template_name = 'event/profile.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Profile')
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена.")
