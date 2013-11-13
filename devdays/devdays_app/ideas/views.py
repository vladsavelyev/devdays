from django.shortcuts import render_to_response
from devdays_app.models import Idea


def index(request, ideaId):
    idea =  Idea.objects.all().get(id=ideaId)
    data =  { 'idea' : idea }
    return render_to_response('idea.html', data)

def list_items(request):
    ideas =  Idea.objects.all()
    data =  { 'ideas' : ideas }
    return render_to_response('ideas.html', data)

