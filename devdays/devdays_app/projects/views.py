from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required
from sqlalchemy.event import Events
from devdays_app.models import Project


def index(request, event):
    """
    Show all projects
    """
    
    return render_to_response('projects/index.html')

@login_required
def new(request):    
    return render_to_response('projects/index.html')
