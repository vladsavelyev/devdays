# coding=utf-8
import datetime
import json
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render_to_response, redirect
from devdays_app.forms import IdeaForm
from devdays_app.models import Idea, Project, Event, Notification


def index_view(request):
    today = datetime.datetime.today()
    #cur_event = Event.objects.filter(date__lte=today)\
    #    .filter(date__gte=today.replace(day=today.day + 3))

    active_event = Event.objects.filter(state='active')
    if active_event.exists():
        e = active_event.get()
    else:
        e = Event.objects.filter(date__lte=datetime.datetime.today())\
                         .order_by('-date')[0]

    return event_view(request,
                      e.date.month,
                      e.date.year)


def event_view(request, month, year):
    e = Event.objects.filter(date__month=month).filter(date__year=year)
    if not e.exists():
        raise Http404
    e = e.get()

    if e.state == 'initial':
        return event_ideas(request, e)
    elif e.state == 'selection':
        return event_project_selection(request, e)
    elif e.state == 'ongoing' or e.state == 'past':
        return event_ongoing(request, e)
    else:
        return HttpResponseBadRequest('bad satus')


def event_ongoing(request, event):
    ns = Notification.objects.filter(event=event)

    ideas = Idea.objects \
                .annotate(num_likes=Count('likes')) \
                .order_by('-num_likes', '-id')
    return render_to_response('event_ongoing.html', {
        'user': request.user,
        'event': event,
        'notifications': ns,
        'events': Event.objects.all().order_by('-date'),
        'ideas': ideas,
    })


def event_ideas(request, event):
    ideas = Idea.objects \
                .annotate(num_likes=Count('likes')) \
                .order_by('-num_likes', '-id')
    return render_to_response('event_ideas.html', {
        'user': request.user,
        'event': event,
        'events': Event.objects.all().order_by('-date'),
        'ideas': ideas
    })


def event_project_selection(request, event):
    ideas = Idea.objects \
                .annotate(num_likes=Count('likes')) \
                .order_by('-num_likes', '-id')
    projects = event.project_set.all()

    return render_to_response('event_project_selection.html', {
        'user': request.user,
        'event': event,
        'projects': projects,
        'events': Event.objects.all().order_by('-date'),
        'ideas': ideas
    })


def start_selection(request, month, year, like_threshold=1, ideas_num=5):
    e = Event.objects.filter(date__month=month).filter(date__year=year)
    if not e.exists():
        raise Http404
    e = e.get()

    e.state = 'selection'
    e.save()

    ideas = Idea.objects \
                .annotate(num_likes=Count('likes')) \
                .filter(num_likes__gte=like_threshold) \
                .order_by('-num_likes', '-id')

    autors = set([i.autor for i in ideas][:ideas_num])

    for i in ideas:
        if i.autor in autors:
            p = Project(idea=i, event=e)
            p.save()
            p.students.add(i.autor)
            p.save()
            autors.remove(i.autor)
    e.save()

    return redirect('/event/%s_%s' % (month, year))


def start_event(request, month, year):
    e = Event.objects.filter(date__month=month).filter(date__year=year)
    if not e.exists():
        raise Http404
    e = e.get()

    e.state = 'ongoing'
    e.save()

    return redirect('/event/%s_%s' % (month, year))


def like_idea(request, idea_id):
    i = Idea.objects.get(id=idea_id)
    if i.likes.all().filter(id=request.user.id).exists():
        return HttpResponseBadRequest()
    else:
        i.likes.add(request.user)
        i.save()
        return HttpResponse(i.id)


def participate(request, event_id, prj_id):
    project = Project.objects.get(id=prj_id)
    if project.students.all().filter(id=request.user.id).exists():
        return HttpResponseBadRequest()

    try:
        event = Event.objects.get(id=event_id)
    except:
        return HttpResponseBadRequest()

    project_id_to_remove = -1
    for p in event.project_set.all():
        for u in p.students.all():
            if request.user == u:
                p.students.remove(request.user)
                project_id_to_remove = p.id

    project.students.add(request.user)
    project.save()
    return HttpResponse(project_id_to_remove)


def project_view(request, id):
    return render_to_response('project.html')


def ideas_view(request):
    return render_to_response('ideas.html')


def ajax_new_idea(request):
    if request.is_ajax():
        print 'ajax, ok'

    print request.GET
    subj = request.GET['all']
    text = request.GET['text']
    idea = Idea(name=subj, description=text, autor=request.user)
    idea.save()

    print 'idea added'

    return HttpResponse(idea.id)

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


def idea_view(request, id):
    idea = Idea.objects.get(id=id)
    return render_to_response('idea.html', {
        'idea': idea,
    })

