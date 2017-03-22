from django.shortcuts import render, HttpResponse, redirect
import random, datetime
from django.utils import formats

# Create your views here.
def index(request):
	if 'total_gold' not in request.session:
		request.session['total_gold'] = 0
		request.session['activities'] = []
	return render(request, 'ninjagold/index.html')


def process(request):
	if request.method == 'POST':
		now = datetime.datetime.now()
		building = request.POST['building']

		buildings = {
			'farm': random.randint(10,20),
			'cave': random.randint(5,10),
			'house': random.randint(2,5),
			'casino': random.randint(-50,50),
		}

		if building in buildings:
			gold =  buildings[building]
			request.session['total_gold'] += gold

		
		formattted_datetime = formats.date_format(now, "SHORT_DATETIME_FORMAT")

		if gold < 0:
			winnings = 'lost'
			activity = {'class': winnings, 'activity':'You went to the {} and lost {} gold. {}'.format(building.upper(), abs(gold), formattted_datetime)}
		else:
			winnings = 'gain'
			activity = {'class': winnings, 'activity':'You went to the {} and gained {} gold! {}'.format(building.upper(), gold, formattted_datetime)}

	request.session['activities'].append(activity)
	request.session.modified = True

	return redirect('ninjagold:index')








