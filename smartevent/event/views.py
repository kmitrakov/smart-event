from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.

def index_event(request):
    return HttpResponse("Страница приложения event.")


def events(request, event_id):
    return HttpResponse(f"Страница события {event_id}.")


def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена.")