from __future__ import unicode_literals

from django.db import models
import re

email_regex = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def validemail(self, email):
		if email_regex.match(email):
			return True
		else:
			return False

class User(models.Model):
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = UserManager()