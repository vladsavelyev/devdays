# coding=utf-8
import datetime
from django.shortcuts import render_to_response, redirect
from devdays_app.models import Idea, Project, Event, UserProfile, Notification


def index_view(request):
    today = datetime.datetime.today()
    #cur_event = Event.objects.filter(date__lte=today)\
    #    .filter(date__gte=today.replace(day=today.day + 3))
    active_event = Event.objects.filter(state='active')
    if active_event.exists():
        return current_event(request, active_event[0])
    else:
        nearest_event = Event.objects.filter(date__lte=datetime.datetime.today()).order_by('date')[0]
        return future_event(request, nearest_event)


def event_view(request, event_id):
    e = Event.objects.get(id=event_id)
    if e.date <= datetime.datetime.today() <= e.date.replace(day=e.date.day + 3):
        return current_event(request, e)
    else:
        return future_event(request, e)



def user_view(request, username):
    u = UserProfile.objects.get(user__username=username)
    return render_to_response('user.html', {
        'user': u,
        'events': Event.objects.all(),
    })



def current_event(request, event):
    ns = Notification.objects.filter(event=event)

    return render_to_response('event.html', {
        'user': request.user,
        'event': event,
        'notifications': ns,
        'events': Event.objects.all(),
        'ideas': Idea.objects.all()
    })


def future_event(request, event):
    return render_to_response('event.html', {
        'user': request.user,
        'event': event,
        'events': Event.objects.all(),
        'ideas': Idea.objects.all()
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
    return render_to_response('project.html')


def ideas_view(request):
    return render_to_response('ideas.html')


def users_view(request):
    return render_to_response('users.html')


def user_view(request, name):
    return render_to_response('user.html')