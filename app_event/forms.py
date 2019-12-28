from django.forms import ModelForm
from django import forms
from app_event.models import Event,Confrim
from django.contrib.admin import widgets  
class DateInput(forms.DateInput):
	input_type='date'
class TimeInput(forms.TimeInput):
	input_type='time'
class Add_event(ModelForm):
	class Meta:
	    model=Event
	    exclude=['creator',]
	    widgets={
	      'date':DateInput(),
	      'time':TimeInput()
	    }




class ConfirmForm(ModelForm):
	class Meta:
		model=Confrim
		fields=('text',)





