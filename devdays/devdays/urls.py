from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

EVENT_PATTERN = r'(?P<month>\d{2})_(?P<year>\d{4})'

urlpatterns = patterns(
    '',
    url(r'^/?$', 'devdays_app.views.index_view'),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),

    url(r'^project/(?P<id>.+)/?', 'devdays_app.views.project_view'),
    url(r'^ideas/?', 'devdays_app.views.ideas_view'),
    url(r'^_ajax_new_idea/?', 'devdays_app.views.ajax_new_idea'),
    url(r'^events/?', 'devdays_app.views.events_view'),
    url(r'^event/' + EVENT_PATTERN, 'devdays_app.views.event_view'),
    url(r'^users/?', 'devdays_app.views.users_view'),
    url(r'^user/(?P<name>.+)/?', 'devdays_app.views.user_view'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
