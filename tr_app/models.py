from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
	text = models.CharField(max_length=200)
	country = models.CharField(max_length=200)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural = 'cities'

	def __str__(self):
		return self.text

class Attraction(models.Model):
	
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		"""Return a string representation of a model"""
		return f"{self.text[:50]}..."