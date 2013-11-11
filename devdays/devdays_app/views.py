# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from devdays_app import Project, Idea


def index(request):
    return render_to_response('index.html')


def projects(request):
    """
    предполагается, что projects это последовательность объектов содержащих поля:
     topic (идея на которой основан проект - foreign key из табицы идей),
     head (руководитель, по умолчанию автор идеи),
     entry (список участников).
    """
    name_title = u'Проекты'
    items = projects
    return render_to_response('topics.html', locals())


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
        ideas = Idea.objects.all()

        return render_to_response('ideas.html', {
            'ideas': [i.name for i in ideas]
        })
    else:
        raise Exception('Creating not implemented')

