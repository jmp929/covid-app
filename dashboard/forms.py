from django import forms
from .models import National, State

class NationalForm(forms.ModelForm):

	class Meta:
		model = National



class StateForm(forms.ModelForm):

	class Meta:
		model = State