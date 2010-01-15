from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'facts.views.index', name='fact_list'),
)

