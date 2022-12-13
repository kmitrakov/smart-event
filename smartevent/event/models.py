from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user_create = models.IntegerField(null=True)
    scope = models.ForeignKey('EventScope', on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event', kwargs={'event_id': self.id})

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-time_create']


class EventScope(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Event Scope'
        verbose_name_plural = 'Event Scopes'
        ordering = ['id']
