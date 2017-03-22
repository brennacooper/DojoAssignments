from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
	return render(request, 'surveyapp/index.html')



def add_user(request):
	
	request.session['name'] = request.POST.get['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']

	return redirect('/results')
	

def show_results(request):
	
	if 'counter' in request.session:
		request.session['counter'] += 1
	else:
		request.session['counter'] = 1

	context = {
	'name': request.session['name'],
	'location': request.session['location'],
	'language': request.session['language'],
	'comment': request.session['comment'],
	'counter': request.session['counter'],

	}


	return render(request, 'surveyapp/results.html', context)