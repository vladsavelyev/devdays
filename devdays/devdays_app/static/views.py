from django.shortcuts import render_to_response


def about(request):
    return render_to_response('static/about.html')


def contacts(request):
    return render_to_response('static/contacts.html')