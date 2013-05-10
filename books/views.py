from django.shortcuts import render,render_to_response
from django.template import RequestContext

# Create your views here.
def morethanagame(request):
	context = {}
	context['description'] = 'more than a game is an awesome book :D'
	return render_to_response('book.html', context, context_instance = RequestContext(request))
def thetownthatneverstared(request):
	context = {}
	context['description'] = 'The town that never stared is an awesome book :D'
	return render_to_response('book.html', context, context_instance = RequestContext(request))
def penaltykick(request):
	context = {}
	context['description'] = 'penalty kick is an awesoem book :D'
	return render_to_response('book.html', context, context_instance = RequestContext(request))
