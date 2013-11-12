from django.conf.urls import patterns, url

urlpatterns = patterns(
    'devdays_app.static.views',
    url(r'about', 'about'),
    url(r'contacts', 'contacts')
)
