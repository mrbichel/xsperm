from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from random import choice, sample

from facts.models import Fact
from testimonials.models import Testimonial

#def funfact(request): 
    #return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

def index(request):
    testimonials = Testimonial.objects.all()[:3]
    facts = Fact.objects.all()[:9]
        
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
        'realize the meaning of life',
        'believers',]
    descriptions = ['hot',
        'big busted',
        'old', 
	'experienced',
        'Russian',
        'sweet',
	'soft',
        '(legal aged) teenage',
        'ripe',
        'hysterical',
        'ovulating',
        'Amazon',
        'extremely ugly',
        'obese',
        'tall',
        'slinky',
        'midget',
        'curly-haired',
        'tall',
        'midget',]
    # Pick two random description
    descriptionSeq = sample(descriptions, 2)
    
    #fact01 = "Sigurd can impregnate %s just by %s." % (choice(objects), choice(actions))
    fact02 = "Sigurd's semen cures %s." % choice(diseases)
    fact03 = "Sigurd's sperm makes %s, %s women %s." % (descriptionSeq[0], descriptionSeq[1], choice(effects))
    funfacts = [fact02, fact03]
    
    return render_to_response('index.html', {
        'testimonials': testimonials,
        'genfact': choice(funfacts),
        'facts': facts,
        }, context_instance=RequestContext(request))
