from django.contrib import admin

from .models import Executive, Gallery, Event

# Register your models here.
admin.site.register(Executive)
admin.site.register(Gallery)
admin.site.register(Event)