from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from random import randint
from datetime import datetime

def index(request):
	if 'yourgold' not in request.session:
		request.session['yourgold'] = 0
		request.session['activity_log']= []
	return render(request, 'ninjagoldapp/index.html')

def process(request):
	building = request.POST['action']
	buildings = {
		'farm': randint(10, 20),
		'cave': randint(5,10),
		'house': randint(2,5),
		'casino': randint(-50,50),
    }
	gold = buildings[building]
	result = {}
	if 'yourgold' in request.session:
		request.session['yourgold'] += gold
	if gold < 0:
		result['sentence'] = "You lost {} gold from the {}. {}".format(abs(gold), building, datetime.now())
		result['color'] = 'red'
	else:
		result['sentence'] = "Earned {} from the {}! {}".format(gold, building, datetime.now())
		result['color'] = 'green'
	request.session['activity_log'].append(result)
	return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')