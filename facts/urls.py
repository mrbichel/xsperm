from django.conf.urls.defaults import *
from facts.models import Fact

urlpatterns = patterns('',
    #url(r'^$', 'facts.views.index', name='prioritize_index'),
    url(r'^add/$', 'facts.views.add_task', name='prioritize_add_task'),
    #rate
)
