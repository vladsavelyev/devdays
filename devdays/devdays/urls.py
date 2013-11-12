from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

EVENT_PATTERN = r'(?P<month>\d{2})_(?P<year>\d{4})/?'

urlpatterns = patterns(
    '',
    url(r'^/?$', 'devdays_app.views.index_view'),
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    
    url(r'^event/' + EVENT_PATTERN, 'devdays_app.events.views.index'),
    url(r'^events/?', 'devdays_app.views.events_view'),
    
    url(r'^idea/(?P<ideaId>\d+)/?', 'devdays_app.ideas.views.index'),
    url(r'^ideas/?', 'devdays_app.ideas.views.list_items'),
    
    url(r'^project/(?P<id>.+)/?', 'devdays_app.views.project_view'),
    
    url(r'^user/(?P<name>.+)/?', 'devdays_app.views.user_view'),
    url(r'^users/?', 'devdays_app.views.users_view'),
    
    url(r'^_ajax_new_idea/?', 'devdays_app.views.ajax_new_idea'),
    
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
