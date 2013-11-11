# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from devdays_app.models import Idea, Project


def index(request):
    return render_to_response('index.html')


def projects(request):
    name_title = u'Проекты'
    projects = Project.objects.all()
    return render_to_response('projects.html', locals())


def ideas(request):
    if request.method == 'GET':
        return render_to_response('ideas.html', {
            'ideas': Idea.objects.all()
        })
    else:
        raise Exception('Creating not implemented')

