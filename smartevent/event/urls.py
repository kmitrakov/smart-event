from django.urls import path

from .views import *

urlpatterns = [
    path('', index_event, name='index'),
    path('<int:event_id>/', events)
]