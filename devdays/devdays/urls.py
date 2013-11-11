from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/?$', 'devdays_app.views.index'),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),

    url(r'^project/(?P<id>.+)/?', 'devdays_app.views.project_view'),
    url(r'^ideas/?', 'devdays_app.views.ideas_view'),
    url(r'^event/(?P<id>.+)/?', 'devdays_app.views.event_view'),
    url(r'^users/?', 'devdays_app.views.users_view'),
    url(r'^user/(?P<name>.+)/?', 'devdays_app.views.user_view'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
