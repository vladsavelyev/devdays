import django
from django.contrib.auth.models import User
from devdays_app.models import Event, ProjectUsers, Project
from django.http import Http404
from django.shortcuts import render_to_response
import devdays_app.models #it is necessary!
from devdays_app.models import Idea
from devdays_app.users.tools import getGravatarUrl


def index(request, userId):
    try:
        user = User.objects.get(id=userId)
    except:
        raise django.http.Http404

    rels = ProjectUsers.objects.all().filter(user=user)
    projects = [rel.project for rel in rels]
    data = {
        'loggedUser': request.user,
        'user': user,
        'userIdeas': Idea.objects.all().filter(author=user.id),
        'userProjects': projects,
        'gravatarUrl': getGravatarUrl(request, user.email, 128),
        'events': Event.objects.all().order_by('-date')
    }
    return render_to_response('user.html', data)
