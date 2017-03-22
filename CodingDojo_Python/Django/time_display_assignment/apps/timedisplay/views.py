from django.shortcuts import render, HttpResponse
from datetime import datetime


def current_datetime(request):
    now = datetime.datetime.now()
# Create your views here.
def index(request):
	date = datetime.now().date().strftime('%B %d, %Y')
	time = datetime.now().time().strftime('%I:%M %p')
	context = {
    	'datetime': [
    		{'date': date},
    		{'time': time},
		]
	}
	return render(request,'timedisplay/index.html', context)

