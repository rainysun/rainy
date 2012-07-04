from django.shortcuts import render_to_response as rtr
from forms import Register, Login
# Create your views here.
def register(req):
	form = Register()
	return rtr('register.html', {
		'form': form
		})

def test(req):
	return rtr('index.html')
