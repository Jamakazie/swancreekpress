from django.shortcuts import render,render_to_response
from django.template import RequestContext

# Create your views here.
def booksindex(request):
	context = {}
	return render_to_response('bookindex.html', context, context_instance = RequestContext(request))
def morethanagame(request):
	context = {}
	context['title'] = "More Than A Game"
	context['url'] = 'http://www.amazon.com/More-Than-Game-Terence-OLeary/dp/0975321609'
	context['description'] = 'During one magical summer three dreams come together and baseball becomes MORE THAN A GAME. Brian McBride leads the league in stolen bases and the Hens to a pennant stretch drive but he cannot run away from the lingering image of his grandfather on his deathbed. MORE THAN A GAME is a story of family, a young man\'s struggle to find his destiny, and the bond baseball spins between fathers and sons.'
	
	return render_to_response('book.html', context, context_instance = RequestContext(request))
def thetownthatneverstared(request):
	context = {}
	context['title'] = "The Town That Never Stared"
	context['url'] = 'http://www.amazon.com/The-Town-That-Never-Stared/dp/0975321617'
	context['description'] = 'A young man\'s love for his brother changes the way a town sees one of America\'s tragic heroes. Epic paintball battles in the woods, Walleye fishing in the Maumee River, and swimming in the ice cold water of Salisbury Quarry fill Cody\'s and Boomer\'s high school summer days. Boomer\'s boyhood dream was to be the Ottawa warrior who stood on top of Buffalo Rock safe-guarding his village. Right out of high school, he joins the army and goes to Iraq. He is horribly injured when he tries to save soldiers trapped in a Humvee destroyed by an IED. As Grand Rapids\' quarterback, Cody followed his big brother\'s blocks on the football field. He is crushed when Boomer leaves home and completely devastated when he visits Boomer in the Brooke Army Medical Center. Stanley Lewinski was a photo-journalist during the War in Viet Nam. With his inspiration, Cody and his granddaughter, Kim embark on a journey to bring Boomer home to The Town That Never Stared.'
	return render_to_response('book.html', context, context_instance = RequestContext(request))
def penaltykick(request):
	context = {}
	context['title'] = 'Penalty Kick'
	context['description'] = 'penalty kick is an awesoem book :D'
	return render_to_response('book.html', context, context_instance = RequestContext(request))
