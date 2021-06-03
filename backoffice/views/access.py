from django.shortcuts import render
from django.forms import *
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class LoginFormView(LoginView):
	template_name = 'access/login.html'
	widgets = {
	   'username': TextInput(
	   	    attrs = {
	   	        'class': 'form-control',
	   	        'placeholder' : 'Enter your password',
	   	        'autocomplete': 'off',
	   	        'rows': 1
	   	    }),
	    'password': TextInput(
	   	    attrs = {
	   	        'class': 'form-control',
	   	        'placeholder' : 'Enter your password',
	   	        'autocomplete': 'off',
	   	        'rows': 1
	   	    })
	}


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['tittle'] = 'Start your session'
		return context


