from django import forms
from .models import *


class EventAddForm(forms.Form):
    title = forms.CharField(max_length=255, label="Title")
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Description", required=False)
    scope = forms.ModelChoiceField(queryset=EventScope.objects.all(), label="Scope", empty_label="Choose Scope")
