import requests

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings

from tr_app.models import City
from tr_app.forms import CityForm

@login_required
def cities(request):
	"""Show all cities."""
	cities = City.objects.filter(owner=request.user).order_by('-date_added')
	context = {'cities': cities}
	return render(request, 'tr_app/cities.html', context)


@login_required
def city(request, city_id):
	"""Show all attractions for the city."""
	city = City.objects.get(id=city_id)
	if city.owner != request.user:
		raise Http404("Get out")
	
	attractions = city.attraction_set.order_by('date_added')
	weather = get_weather(request, city)
	context = {'city': city, 'attractions': attractions, 'weather': weather}
	return render(request, 'tr_app/city.html', context)


def get_weather(request, city):
	"""Show city weather"""
	url = f"http://api.openweathermap.org/data/2.5/weather?q={city.text},{city.country}&units=metric&APPID={settings.API_KEY}"
	response = requests.get(url)
	data = response.json()
	return data


@login_required
def new_city(request):
	"""Add a new city"""
	if request.method != 'POST':
		# No data submitted, create a blank form
		form = CityForm()
	else:
		# Post data submitted, process data
		form = CityForm(data=request.POST)
		if form.is_valid():
			new_city = form.save(commit=False)
			new_city.owner = request.user
			new_city.save()
			return redirect('tr_app:cities')

	# Display blank or individual form
	context = {'form': form}
	return render(request, 'tr_app/new_city.html', context)


@login_required
def edit_city(request, city_id):
	"""Edit an existing attraction"""
	city = City.objects.get(id = city_id)

	if request.method != 'POST':
		# Initial request, pre-fill form with the current info
		form = CityForm(instance=city)
	else:
		# Post data submitted, process data
		form = CityForm(instance=city, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('tr_app:city', city_id=city.id)
		
	context = {'city': city, 'form': form}
	return render(request, 'tr_app/edit_city.html', context)


def delete_city(request, city_id):
	"""Delete a city"""
	
	city = City.objects.get(id=city_id)
	
	if request.method =="POST":
		city.delete()
        # after deleting redirect to home page
		return redirect('tr_app:cities')
		
	context ={'city': city}
	return render(request, "tr_app/delete_city.html", context)