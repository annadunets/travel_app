from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
	"""Register a new user"""
	if request.method != 'POST':
		# Blank form
		form = UserCreationForm()
	else:
		# Completed form 
		form = UserCreationForm(data=request.POST)
		new_user = form.save()
		login(request, new_user)
		return redirect('tr_app:index')

	context = {'form': form}
	return render(request, 'registration/register.html', context)