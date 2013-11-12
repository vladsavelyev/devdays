from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required
from devdays_app.models import Event


def index(request, month, year):
    # TODO: if event.state == active
    return chartActive(request, month, year)

def chartActive(request, month, year):
    data = {
        'event' : Event.objects.get(date__year = int(year), date__month = int(month))
    }
    return render_to_response('events/chartActive.html', data)