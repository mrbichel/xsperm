from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'facts.views.index', name='fact_list'),
    url(r'^rate/(?P<id>\d+)/(?P<action>\w+)/$', 'facts.views.rate', name='fact_rate'),
)

