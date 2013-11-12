from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

EVENT_PATTERN = r'(?P<month>\d{2})_(?P<year>\d{4})/?'

urlpatterns = patterns(
    '',
    (r'^/?$', 'devdays_app.views.index_view'),
    (r'^openid/', include('django_openid_auth.urls')),
    (r'^logout/$', 'django.contrib.auth.views.logout'),
    (r'^events/' + EVENT_PATTERN, 'devdays_app.events.views.index'),
    (r'^events/?', 'devdays_app.views.events_view'),
    (r'^project/(?P<id>.+)/?', 'devdays_app.views.project_view'),
    (r'^ideas/?', 'devdays_app.views.ideas_view'),
    (r'^_ajax_new_idea/?', 'devdays_app.views.ajax_new_idea'),
    (r'^users/?', 'devdays_app.views.users_view'),
    (r'^user/(?P<name>.+)/?', 'devdays_app.views.user_view'),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
