from django.contrib import admin
from .models import Venue, MyClubUser, Event


# admin.site.register(Venue)
# admin.site.register(MyClubUser)
# admin.site.register(Event)



@admin.register(Venue)
class VenueModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'zip_code', 'phone', 'web', 'email_address']
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(MyClubUser)
class MyClubUserModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']

@admin.register(Event)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ['name','event_date', 'venue', 'manager', 'display_attendees', 'description']
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)
    fieldsets = (
        ('Required Information', {
            'description': "These fields are required for each event.",
            'fields': (('name','venue'), 'event_date')
        }),
        ('Optional Information', {
            'classes': ('collapse',),
            'fields': ('description', 'manager')
        }),
        )