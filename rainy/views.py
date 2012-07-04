from django.shortcuts import render_to_response as rtr

def home(req):
	return rtr('index.html')
