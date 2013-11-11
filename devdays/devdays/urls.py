from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^/?$', 'devdays_app.views.index'),

    url(r'^admin/', include(admin.site.urls)),
)


