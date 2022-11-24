"""Defines URL patterns for travel app"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from tr_app.views import index
from tr_app.views import cities_view
from tr_app.views import attractions_view


app_name = 'tr_app'
urlpatterns = [
	# Home page
	path('', index, name='index'),
	# Page that shows all the cities
	path('cities/', cities_view.cities, name='cities'),
	# Page that shows all the attractions in the city
	path('cities/<int:city_id>', cities_view.city, name='city'),
	# Page for adding a new city
	path('new_city/', cities_view.new_city, name='new_city'),
	# Page for editing a city
	path('edit_city/<int:city_id>', cities_view.edit_city, name='edit_city'),
	# Page for deleting city
	path('delete_city/<int:city_id>', cities_view.delete_city, name='delete_city'),
	# Page for adding a new attraction
	path('new_attraction/<int:city_id>', attractions_view.new_attraction, name='new_attraction'),
	# Page for editing an attraction
	path('edit_attraction/<int:attraction_id>', attractions_view.edit_attraction, name='edit_attraction'),
	# Page for deleting attraction
	path('delete_attraction/<int:attraction_id>', attractions_view.delete_attraction, name='delete_attraction'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)