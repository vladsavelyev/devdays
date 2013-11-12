from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required
from devdays_app.models import Event


def index(request, event_date):
    # TODO: if event.state == active
    return chartActive(request, event_date)

def chartActive(request, event_date):
    spl = str(event_date).split('_')
    event = Event.objects.filter(date__year = spl[0], date__month = spl[1])
    return render_to_response('events/chartActive.html', event)
