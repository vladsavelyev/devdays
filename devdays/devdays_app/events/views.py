from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required
from devdays_app.models import Event


def index(request, event_date):
    # TODO: if event.state == active
    return chartActive(request, event_date)

def chartActive(request, event_date):
    spl = str(event_date).split('_')
    data = {
        'event' : Event.objects.get(date__year = int(spl[1]), date__month = int(spl[0]))
    }
    return render_to_response('events/chartActive.html', data)
