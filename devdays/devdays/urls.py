from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/?$', 'devdays_app.views.index'),
    url(r'^projects', 'devdays_app.views.projects'),
    url(r'^projects/new', 'devdays_app.views.projects'),
    url(r'^admin/', include(admin.site.urls)),
)


