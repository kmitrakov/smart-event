from django.db import models


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=255)
    status = models.IntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    user_create = models.IntegerField(null=True)


    def __str__(self):
        return self.title
