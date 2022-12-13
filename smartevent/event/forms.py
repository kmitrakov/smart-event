from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class EventAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['scope'].empty_label = "Select Scope"

    class Meta:
        model = Event
        fields = ['title', 'description', 'scope']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input-text'}),
            'description': forms.Textarea(attrs={'class': 'form-input-textarea', 'cols': 60, 'rows': 10}),
            'scope': forms.Select(attrs={'class': 'form-select'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 255:
            raise ValidationError('Title more then 255')

        return title


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input-text'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input-text'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input-password'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-input-password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-input-text'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input-password'}))