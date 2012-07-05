from forms import Register, Login
from django.shortcuts import render_to_response as rtr, redirect
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.models import User
from userprofile.models import UserProfile, Facebook
from django.contrib import messages
# Create your views here.
@csrf_protect
def register(req):
	if req.method == 'POST':
		form = Register(req.POST)
		if form.is_valid():
			try:
				user = User.objects.get(username = req.POST.get('name'))
			except:
				user = None
			if user is not None:
				messages.error(req, 'User name exist!')
				return redirect('/account/register/')
			return redirect('/')
	else:
		form = Register()
	return rtr('register.html', {
		'form': form
	}, RequestContext(req, {}))


def test(req):
	return rtr('index.html')
