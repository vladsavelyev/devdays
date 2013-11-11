# coding=utf-8
from django.shortcuts import render_to_response
from devdays_app.models import Idea, Project, Event


def index(request):
    # ищем ивенты с сегодняшней датой
    # если нашелся, то берем сегодняший.
    # если нет, то наступающий.
    event = Event.objects.all()[0]
    return event_view(event.id, request)


def event_view(event_id, request):
    # если ивент идет:
    # список проектов

    # если будет:
    # список идей

    return render_to_response('event.html', {
        'user': request.user,
    })


#def projects(request):
#    name_title = u'Проекты'
#    projects = Project.objects.all()
#    return render_to_response('projects.html', locals())
#
#
#def ideas(request):
#    if request.method == 'GET':
#        return render_to_response('ideas.html', {
#            'ideas': Idea.objects.all()
#        })
#
#    else:
#        raise Exception('Creating is not implemented')
#

def project_view(request, id):
    return render_to_response('project_view.html')


def ideas_view(request):
    return render_to_response('ideas_view.html')


def users_view(request):
    return render_to_response('users_view.html')


def user_view(request, name):
    return render_to_response('user_view.html')