from django.shortcuts import render_to_response
from devdays.devdays_app.models import Project


def add(request):
    dict = {'message': 'hello'}
    p = Project()

    return render_to_response('projects/index.html', dict)
