from tr_app.views.cities_view import *
from tr_app.views.attractions_view import *
from django.shortcuts import render

from tr_app.models import City, Attraction
from tr_app.forms import CityForm, AttractionForm

def index(request):
	"""Home page for Travel app"""
	return render(request, 'tr_app/index.html')