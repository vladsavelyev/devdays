from django.shortcuts import render_to_response

def add(request):
    dict = {'message': 'hello'}
    return render_to_response('projects/index.html', dict)