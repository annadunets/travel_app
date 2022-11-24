from django import forms

from .models import City
from .models import Attraction

class CityForm(forms.ModelForm):

	class Meta:
		model = City
		fields = ['text', 'country']
		labels = {'text': '', 'country': ''}
		widgets = {
			'text': forms.TextInput(attrs={
				'placeholder': 'city name'
			}),
			'country': forms.TextInput(attrs={
				'placeholder': 'country'
			})
		}
		
class AttractionForm(forms.ModelForm):
	class Meta:
		model = Attraction
		fields = ['text']
		labels = {'text': ''}