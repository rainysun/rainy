from django import forms

class Register(forms.Form):
	fbid = forms.BooleanField(required=True)
	name = forms.CharField(max_length=50)
	email= forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput, label="Your Password")
class Login(forms.Form):
	name	 = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput, label="Your Password")
