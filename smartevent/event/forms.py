from django import forms
from django.core.exceptions import ValidationError

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
            'description': forms.Textarea(attrs={'class': 'form-input-textarea', 'cols': 60, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 255:
            raise ValidationError('Title more then 255')

        return title