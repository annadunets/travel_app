from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf import settings

from tr_app.models import City, Attraction
from tr_app.forms import AttractionForm


@login_required
def new_attraction(request, city_id):
	"""Add a new attraction"""
	city = City.objects.get(id=city_id)

	if request.method != 'POST':
		# No data submitted, create a blank form
		form = AttractionForm()
	else:
		# Post data submitted, process data
		form = AttractionForm(data=request.POST)
		if form.is_valid():
			new_attraction = form.save(commit=False)
			new_attraction.city = city
			new_attraction.save()
			return redirect('tr_app:city', city_id = city_id)

	# Display blank or individual form
	context = {'city':city, 'form': form}
	return render(request, 'tr_app/new_attraction.html', context)


@login_required
def edit_attraction(request, attraction_id):
	"""Edit an existing attraction"""
	attraction = Attraction.objects.get(id = attraction_id)
	city = attraction.city

	if request.method != 'POST':
		# Initial request, pre-fill form with the current info
		form = AttractionForm(instance=attraction)
	else:
		# Post data submitted, process data
		form = AttractionForm(instance=attraction, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('tr_app:city', city_id=city.id)
		
	context = {'attraction': attraction, 'city': city, 'form': form}
	return render(request, 'tr_app/edit_attraction.html', context)


def delete_attraction(request, attraction_id):
    """Delete an attraction"""
    
    attraction = Attraction.objects.get(id=attraction_id)
    city = attraction.city
    
    if request.method =="POST":
        attraction.delete()
        # after deleting redirect to home page
        return redirect('tr_app:city', city_id=city.id)
		
    context ={'attraction': attraction}
    return render(request, "tr_app/delete_attraction.html", context)