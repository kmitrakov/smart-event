from django.urls import path

from .views import *

urlpatterns = [
    path('', EventIndex.as_view(), name='index'),
    path('event/<int:event_id>/', EventShow.as_view(), name='event'),
    path('eventadd/', EventAdd.as_view(), name='event_add'),
    path('contact/', Contact.as_view(), name='contact'),
    path('about/', About.as_view(), name='about'),
    path('signin/', SignIn.as_view(), name='sign_in'),
    path('signout/', SignOut.as_view(), name='sign_out'),
    path('signup/', SignUp.as_view(), name='sign_up'),
    path('myspace/', MySpace.as_view(), name='my_space'),
    path('forgotpassword/', ForgotPassword.as_view(), name='forgot_password')
]
