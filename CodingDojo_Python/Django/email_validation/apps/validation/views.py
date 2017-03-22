from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	return render(request, 'validation/index.html')

def validate(request):
	if User.objects.validemail(request.POST['email']):
		User.objects.create(email = request.POST['email'])
		messages.success(request, 'The email address you entered (' + request.POST['email'] + ') is a VALID email address! Thank you!')
		return redirect (reverse('success'))
	else:
		messages.warning(request, 'Email is not valid!')
		return redirect('/')

def success(request):
	context = {
		"emails": User.objects.all()
	}
	return render(request, 'validation/success.html', context)