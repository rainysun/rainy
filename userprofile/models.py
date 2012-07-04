from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	fbid = models.BooleanField()
	vip  = models.BooleanField()
	balance = models.CharField(max_length=10)
class Facebook(models.Model):
	user = models.ForeignKey(User, unique=True)
	fbid = models.BigIntegerField()
	name = models.CharField(max_length=50)
	email= models.EmailField()
