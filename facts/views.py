from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from facts.models import Fact
from facts.forms import FactForm
        
def index(request):
    facts = Fact.objects.all()
    if request.method == 'POST':
        form = FactForm(request.POST)
        if form.is_valid():
            fact = form.save()         
            return HttpResponseRedirect(reverse('fact_list'))        
    else:
        form = FactForm()
    return render_to_response('facts/index.html',
        {'form': form,
        'facts': facts,},
        context_instance = RequestContext(request))
    
def rate(request, id, action):
    fact = Fact.objects.get(pk=id)
    
    if action == 'up':
        fact.rating += 1
    elif action == 'down':
	fact.rating += -1
    
    fact.save()
    return HttpResponseRedirect(reverse('fact_list'))

