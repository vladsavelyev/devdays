from django.conf.urls import patterns, url

urlpatterns = patterns(
    'devdays_app.projects.views',
    url(r'^(?P<event>\d{4}_\d)/', 'index'),
    url(r'new', 'index'),
)