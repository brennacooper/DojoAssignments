from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
	User.userManager.login ("speros@codingdojo.com","Speros")
	return HttpResponse(User.userManager.login ("speros@codingdojo.com","Speros"))





# 	print("Running index method, calling out to User.")
# 	user = User.objects.login("speros@codingdojo.com","Speros")
# # DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
# 	print (type(user))
# 	if 'error' in user:
# 		pass
# 	if 'theuser' in user:
# 		pass
	