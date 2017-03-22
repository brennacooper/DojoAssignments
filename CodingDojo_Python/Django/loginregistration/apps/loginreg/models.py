from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def register_user(self, postData):
		errors = []

		if len(postData['first_name']) < 2:
			errors.append('First name must be at least 2 characters long.')

		if len(postData['last_name']) < 2:
			errors.append('Last name must be at least 2 characters long.')

		if not len(postData['email']) < 2:
			errors.append('Email required.')

		else:
			if not EMAIL_REGEX.match(postData['email']):
				errors.append('Please enter a valid email.')

		if len(postData['passsword']) < 8:
			errors.append('Password name must be at least 8 characters long.')

		if len(postData['password_confirmation']) < 2:
			errors.append('Password confirmation must be at least 8 characters long.')

		
		if not postData['password'] == postData['password_confirmation']:
			errors.append('Password fields must match.')

		if self.filter(email = postData['email']):
			errors.append('Please enter a unique email.')

		response_to_views = {}

		if not errors:
			hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			user = self.create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = hashed_password)
			response_to_views['user'] = user
			response_to_views['status'] = True

		else:
			response_to_views['errors'] = errors



	def login((self, postData):
		user = self.filter(email = postData['email'])
		response_to_views = {}
		
		if not user:
			response_to_views['status'] = False
			response_to_views['user'] = 'user.first()

		else:
			if not bcrypt.checkpw(postData['password'].encode(), user[0].password):
				response_to_views['status'] = True
				response_to_views['errors'] = 

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()