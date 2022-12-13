from django import template
from event.models import *

register = template.Library()


@register.simple_tag()
def get_events(scope=None):
    if not scope:
        return Event.objects.all()
    else:
        return Event.objects.filter(scope=scope)
