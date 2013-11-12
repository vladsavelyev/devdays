from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from forms import CreateIdea
from django.contrib.auth.decorators import login_required
from sqlalchemy.event import Events
from devdays_app.models import Project, Idea


def index(request, event):
    """
    Show all projects
    """
    
    return render_to_response('projects/index.html')

@login_required
def new(request):
    if request.method == 'POST':
        form = CreateIdea(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Idea.objects.create(**cd)
        else:
            form = CreateIdea()
            return render_to_response('projects/new.html', {'form': form})
    return HttpResponse()

