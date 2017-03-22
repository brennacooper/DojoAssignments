from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	return render (request, 'loginreg/index.html')

def register(request, ):
	response_from_models = User_objects.register_user(request.POST)

	if response_from_models ['status']:
		request.session ['user_id'] = response_to_models['user'].id

		return redirect('users:success')

def login:


def success:
	if not 'user_id' in request.session:
		messages.error(request, 'Must be logged in!')
