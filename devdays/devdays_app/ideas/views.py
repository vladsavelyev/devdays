from django.http import HttpResponseForbidden
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from devdays_app.models import Idea, Event




def idea_view(request, ideaId):
    idea = Idea.objects.get(id=ideaId)
    return render_to_response('idea/idea.html', {
        'loggedUser' : request.user,
        'events': Event.objects.all().order_by('-date'),
        'idea': idea,
    })

def idea_edit(request, ideaId):
    idea = Idea.objects.get(id=ideaId)
    if request.user != idea.author:
        return HttpResponseForbidden()
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['description']
        idea.name = title
        idea.description = desc
        idea.save()
    
    data = {
        'loggedUser' : request.user,
        'events': Event.objects.all().order_by('-date'),
        'idea': idea,   
    }
    data.update(csrf(request))
    return render_to_response('idea/edit.html', data)

