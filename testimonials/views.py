from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from testimonials.models import Testimonial
from testimonials.forms import TestimonialForm
        
def index(request):
    testimonials = Testimonial.objects.all()
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save()         
            return HttpResponseRedirect(reverse('testimonial_list'))        
    else:
        form = TestimonialForm()
    return render_to_response('testimonials/index.html',
        {'form': form,
        'testimonials': testimonials,},
        context_instance = RequestContext(request))
    
