from __future__ import unicode_literals
from django.db import models
  #Our new manager!
  #No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
	def login(self, email, password):
		print ("login logic here!")
		print ("If successful login occurs, pass back a tuple with (True, user)")
		print ("If unsuccessful return a tuple with (False, 'Login unsuccessful')")
		return ("I will be a future login mathod amde by coding dojo students!")
	
	def register(self, **kwargs):
		print ("Register login here")
		print ("If successful login occurs, pass back a tuple with (True, user)")
		print ("If unsuccessful return a tuple with (False, 'Login unsuccessful')")
		pass

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	# *************************
	# Connect an instance of UserManager to our User model overwriting
	# the old hidden objects key with a new one with extra properties!!!
	userManager = UserManager()
	# *************************
