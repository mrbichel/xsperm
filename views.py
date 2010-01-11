from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from facts.models import Fact
from testimonials.models import Testimonial

def index(request):
    testimonials = Testimonial.objects.all()
    facts = Fact.objects.all()
    
    return render_to_response('index.html', {
        'testimonials': testimonials,
        'facts': facts
        }, context_instance=RequestContext(request))
