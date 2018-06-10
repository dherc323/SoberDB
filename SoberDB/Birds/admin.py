from django.contrib import admin
########## Register your models here:
"""
This code tells the Django admin site to offer an interface for
each of these models
"""

class BirdAdmin(admin.ModelAdmin):
    list_display = ('BirdID','Location','Experimenter','Alive','Age',)
    search_fields = ('BirdID','Location','Experimenter',
    'Alive','Age','Parent','Procedure','Experimenter','Parent',)
    list_filter = ('Experimenter',)


from .models import Finch
admin.site.register(Finch, BirdAdmin)
