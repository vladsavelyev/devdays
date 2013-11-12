from django.contrib.auth.models import User
from django.shortcuts import render_to_response
import devdays_app.models #it is necessary!

def index(request, userId):
    data = { 'user': User.regular_users.get(id=int(userId))}
    return render_to_response('user.html', data)


def list_users(request):
    data = { 'users': User.regular_users }
    return render_to_response('users.html', data)