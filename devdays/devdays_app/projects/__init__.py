from django.shortcuts import render_to_response
from devdays.devdays_app.models import Project, Event
from django.contrib.auth.decorators import login_required



def index(request, event):
    """
    Show all projects
    """
    
    return render_to_response('projects/index.html')

@login_required
def new(request):
    dict = {'message': 'hello'}
    p = Project()
    return render_to_response('projects/index.html', dict)
