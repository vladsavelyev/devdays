from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

EVENT_PATTERN = r'(?P<month>\d{2})_(?P<year>\d{4})/?'

urlpatterns = patterns(
    '',
    url(r'^/?$', 'devdays_app.views.index_view'),
    url(r'^about/?$', 'devdays_app.static.views.about'),
    url(r'^contacts/?$', 'devdays_app.static.views.contacts'),
    
    url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    
    url(r'^event/' + EVENT_PATTERN, 'devdays_app.views.event_view'),
    #url(r'^events/?', 'devdays_app.views.events_view'),
    url(r'^start_event/' + EVENT_PATTERN, 'devdays_app.views.start_event'),
    url(r'^start_selection/' + EVENT_PATTERN, 'devdays_app.views.start_selection'),
    url(r'^like_idea/(?P<idea_id>\d+)/?', 'devdays_app.views.like_idea'),
    url(r'^participate/(?P<prj_id>\d+)/?', 'devdays_app.views.participate'),

    url(r'^idea/(?P<id>\d+)/?', 'devdays_app.views.idea_view'),
    url(r'^ideas/?', 'devdays_app.ideas.views.list_items'),
    
    url(r'^project/(?P<id>\d+)/?', 'devdays_app.views.project_view'),
    
    url(r'^user/(?P<userId>\d+)/?', 'devdays_app.users.views.index'),
    url(r'^users/?', 'devdays_app.users.views.list_users'),
    
    url(r'^_ajax_new_idea/?', 'devdays_app.views.ajax_new_idea'),
    
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
