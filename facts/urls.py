from django.conf.urls.defaults import *
from facts.models import Fact

urlpatterns = patterns('',
    url(r'^$', 'facts.views.index', name='fact_list'),
    #rate
)

