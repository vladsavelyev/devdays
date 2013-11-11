from django.shortcuts import render
from django.shortcuts import render_to_response
from devdays_app import Project


def index(request):
    return render_to_response('index.html')


def projects(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        return render_to_response('projects.html', {'projects', [p.name for p in projects]})
    else:
        raise Exception('Creating not implemented')


































































