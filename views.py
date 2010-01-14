from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from random import choice

from facts.models import Fact
from testimonials.models import Testimonial

#def funfact(request): 
    #return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

    

def index(request):
    testimonials = Testimonial.objects.all()
    facts = Fact.objects.all()
        
    objects = ['a kangaroo',
        'a mailbox',
        'a women',]
    actions = ['walking by it', 
        'gazing at it', 
        'thinking about it', 
        'talking to it', ]
    diseases = ['xenophobia', 
        'arachnophobia', 
        'cancer', 
        'hydrophobia', 
        'AIDS', 
        'nymphomania', 
        'H1N1', 
        'avian flu', 
        'SARS',
        'mad cow disease',
        'ADHD',]
    effects = ['go moist', 
        'warm', 
        'energetic',
        'daydream',
        'think about their fathers',
        'cry with joy',
        'dance',
        'sing',
        'sigh',
        'moan',
        'gaze at the stars',
        'have well formed octuplets',
        'realize the meaning of life',]
    descriptions = ['hot and curly', 
        'big busted',
        'old and experienced',
        'Russian',
        'sweet and soft',
        'teenage (legal aged)',
        'ripe',
        'hysterical',
        'ovulating',
        'Amazon',
        'extremely ugly',
        'obese',
        'tall and slinky',
        'midget',]
    
    #fact01 = "Sigurd can impregnate %s just by %s." % (choice(objects), choice(actions))
    fact02 = "Sigurd's semen cures %s." % choice(diseases)
    fact03 = "Sigurd's sperm makes %s women %s." % (choice(descriptions), choice(effects))
    funfacts = [fact02, fact03]
    
    return render_to_response('index.html', {
        'testimonials': testimonials,
        'genfact': choice(funfacts),
        'facts': facts,
        }, context_instance=RequestContext(request))
