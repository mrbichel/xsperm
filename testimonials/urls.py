from django.conf.urls.defaults import *

urlpatterns = patterns('',
   url(r'^$', 'testimonials.views.index', name='testimonial_list'),
)
