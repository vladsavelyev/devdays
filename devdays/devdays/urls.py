from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

EVENT_PATTERN = r'(?P<event_date>\d{2}_\d{4})'

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/?$', 'devdays_app.views.index_view'),
    url(r'^', include('devdays_app.static.urls')),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^projects/', include('devdays_app.projects.urls')),
    url(r'^events/', include('devdays_app.events.urls')),
    url(r'^ideas/?', 'devdays_app.views.ideas_view'),
    url(r'^users/?', 'devdays_app.views.users_view'),
    url(r'^user/(?P<name>.+)/?', 'devdays_app.views.user_view'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
