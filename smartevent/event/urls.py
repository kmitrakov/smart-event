from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:event_id>/', events),
    path('about/', about, name='about')
]
