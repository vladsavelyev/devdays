from django.conf.urls import patterns, url

EVENT_PATTERN = r'(?P<event>\d{2}_\d{4})' 

urlpatterns = patterns(
    'devdays_app.projects.views',
    url(EVENT_PATTERN + '/', 'index'),
    url(EVENT_PATTERN + '/new', 'index'),
)
