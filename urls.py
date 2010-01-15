from django.conf.urls.defaults import *
from xsperm import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'views.index', name='index'),
    (r'^facts/', include('xsperm.facts.urls')),
    (r'^facts/', include('xsperm.testimonials.urls')),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)



# Serve static media through django if we are on a development server
if settings.DEVELOPMENT_MODE:
    urlpatterns += patterns('django.views',
        url(r'%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'static.serve', {
            'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
    )
