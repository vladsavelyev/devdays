from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/?$', 'devdays_app.views.index'),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^projects/', include('devdays_app.projects.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^ideas', 'devdays_app.views.ideas'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
