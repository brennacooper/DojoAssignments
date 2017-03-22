from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	return render(request, 'ninjasapp/index.html')

def all_ninjas(request):
	context = {
		'allninjas': True,
	}
	return render(request, 'ninjasapp/ninjas.html', context)

def one_ninja(request, color):
	if color == 'blue' or color == 'orange' or color == 'red' or color == 'purple':
		context = {
			'allninjas': False,
			'color': color,
		}
	else: 
		context = {
			'allninjas': False,
			'april': True,
		}

	return render(request, 'ninjasapp/ninjas.html', context)