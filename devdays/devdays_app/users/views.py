from django.contrib.auth.models import User
from django.shortcuts import render_to_response
import devdays_app.models #it is necessary!
from devdays_app.users.tools import getGravatarUrl


def index(request, username):
    user = User.objects.get(username=username)
    data = { 
        'user': user,
        'gravatarUrl': getGravatarUrl(request, user.email, 128)
    }
    return render_to_response('user.html', data)


def list_users(request):
    data = { 'users': User.objects.all() }
    return render_to_response('users.html', data)