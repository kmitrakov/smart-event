from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:event_id>/', events, name='events'),
    path('about/', about, name='about'),
    path('eventadd/', eventadd, name='eventadd'),
    path('contact/', contact, name='contact'),
    path('signin/', signin, name='signin')
]
