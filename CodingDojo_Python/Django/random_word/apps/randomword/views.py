from django.shortcuts import render, redirect, HttpResponse
import random
import string


# Create your views here.


def index(request):
	new_word = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(14)])
	if 'counter' not in request.session:
		request.session['counter'] = 1
	

	context = {
		'word': new_word,
		'counter': request.session['counter'],

	}

	return render (request, 'randomword/index.html', context)


def randomword(request):
	request.session['counter'] +=1

	return redirect('/')

 