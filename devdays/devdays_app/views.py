# coding=utf-8
import datetime
from django.db.models import Count
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect
from devdays_app.forms import IdeaForm
from devdays_app.models import Idea, Project, Event, UserProfile, Notification


def index_view(request):
    today = datetime.datetime.today()
    #cur_event = Event.objects.filter(date__lte=today)\
    #    .filter(date__gte=today.replace(day=today.day + 3))

    active_event = Event.objects.filter(state='active')
    if active_event.exists():
        e = active_event.get()
    else:
        e = Event.objects.filter(
            date__lte=datetime.datetime.today()).order_by('date').get()

    return event_view(request,
                      e.date.month,
                      e.date.year)


def event_view(request, month, year):
    e = Event.objects.filter(date__month=month).filter(date__year=year)
    if not e.exists():
        raise Http404()
    e = e.get()

    if e.state == 'initial':
        return event_ideas(request, e)
    elif e.state == 'selection':
        return event_project_selection(request, e)
    elif e.state == 'ongoing' or e.state == 'past':
        return event_ongoing(request, e)
    else:
        return event_ongoing(request, e)
        return HttpResponseBadRequest('bad satus')


def user_view(request, username):
    u = UserProfile.objects.get(user__username=username)
    return render_to_response('user.html', {
        'user': u,
        'events': Event.objects.all(),
    })


def event_ongoing(request, event):
    ns = Notification.objects.filter(event=event)

    ideas = Idea.objects \
                .annotate(num_likes=Count('likes')) \
                .order_by('-num_likes', '-id')

    return render_to_response('event_ongoing.html', {
        'user': request.user,
        'event': event,
        'notifications': ns,
        'events': Event.objects.all(),
        'ideas': ideas,
    })


def event_ideas(request, event):
    return render_to_response('event_ideas.html', {
        'user': request.user,
        'event': event,
        'events': Event.objects.all(),
        'ideas': Idea.objects.all().order_by('-id')
    })


def event_project_selection(request, event):
    return render_to_response('event_project_selection.html', {
        'user': request.user,
        'event': event,
        'events': Event.objects.all(),
        'ideas': Idea.objects.all().order_by('-id')
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


def ajax_new_idea(request):
    if request.is_ajax():
        print 'ajax, ok'

    print request.GET
    subj = request.GET['all']
    text = request.GET['text']
    idea = Idea(name=subj, description=text, autor=UserProfile.objects.all()[0])
    idea.save()

    print 'idea added'

    return HttpResponse()

    #form = IdeaForm(request.POST or None)
    #
    #if request.method == "POST" and request.is_ajax():
    #    print request.POST
    #
    #    if form.is_valid():
    #        idea = Idea(name=form.subject, description=form.text)
    #        idea.save()
    #        msg = "AJAX submission saved"
    #    else:
    #        msg = "AJAX post invalid"
    #else:
    #    msg = "GET petitions are not allowed for this view."


def events_view(request):
    return render_to_response('events_view.html')