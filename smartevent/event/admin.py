from django.contrib import admin

from .models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'time_create', 'time_update', 'user_create', 'scope')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'scope')
    list_editable = ('scope',)
    list_filter = ('scope',)

class EventScopeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Event, EventAdmin)
admin.site.register(EventScope, EventScopeAdmin)
