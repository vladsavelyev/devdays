# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from devdays_app import Project, Idea


def index(request):
    return render_to_response('index.html')


def ideas(request):
    if request.method == 'GET':
        ideas = Idea.objects.all()

        return render_to_response('ideas.html', {
            'ideas': [i.name for i in ideas]
        })
    else:
        raise Exception('Creating not implemented')

