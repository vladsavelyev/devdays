# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from devdays_app.models import Idea


def index(request):
    return render_to_response('index.html')


def projects(request):
    name_title = u'Проекты'
    projects = Project.objects.all()
    return render_to_response('projects.html', locals())


def topics(request):
    """
    предполагается, что topics это последовательность объектов содержащих поля:
     heading (название),
     description (описание),
     autor (автор).
    """
    name_title = u'Идеи'
    items = topics
    return render_to_response('topics.html', locals())


def ideas(request):
    if request.method == 'GET':
        return render_to_response('ideas.html', {
            'ideas': Idea.objects.all()
        })

    else:
        raise Exception('Creating is not implemented')

