# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from devdays_app.models import Idea


def index(request):
    return ideas(request)


def ideas(request):
    if request.method == 'GET':
        return render_to_response('ideas.html', {
            'ideas': Idea.objects.all()
        })

    else:
        raise Exception('Creating is not implemented')

