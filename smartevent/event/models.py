from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=255)
    status = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user_create = models.IntegerField(null=True)
    scope = models.ForeignKey('EventScope', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events', kwargs={'event_id': self.pk})


class EventScope(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
