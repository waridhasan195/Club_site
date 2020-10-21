from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Event
from django.http import HttpResponseRedirect
from .forms import VenueForm



def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year <2000 or year > 2099: year = date.today().year
    month_name = calendar.month_name[month]
    title = "Myclub Event calender - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    announcements = [
                        {
                            'date': '6-10-2020',
                            'announcement': "Club Registrations Open"
                        },
                        {
                            'date': '6-15-2020',
                            'announcement': "Joe Smith Elected New Club President"
                        }
                ]
    context = {'title':title, 'cal':cal, 'announcements':announcements}
    return render(request, 'events/calendar_base.html', context)


def all_events(request):
    event_list = Event.objects.all()
    context = {'event_list':event_list}
    return render(request,'events/event_list.html',context)


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})