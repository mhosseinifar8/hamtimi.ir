from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ('username','password',)
		def __init__(self, *args, **kwargs):
			super().__init__(*args,**kwargs)
			del self.fields['password2']

		  
		  



		
