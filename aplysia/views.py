from django.shortcuts import render_to_response as rtr
#import rainy
# Create your views here.
def index(req):
	return rtr('aplysia/index.html', {
		'title': 'Aplysia',
		'css': 'aplysia_base'
		})
