from django.shortcuts import render_to_response
from devdays.devdays_app.models import Project
from django.contrib.auth.decorators import login_required


@login_required
def new(request):
    dict = {'message': 'hello'}
    p = Project()
    return render_to_response('projects/index.html', dict)
