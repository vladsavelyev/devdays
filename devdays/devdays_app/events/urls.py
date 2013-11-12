from django.conf.urls import patterns, url
from devdays.urls import EVENT_PATTERN

urlpatterns = patterns(
    'devdays_app.events.views',
    url(EVENT_PATTERN + '/', 'index'),
)
