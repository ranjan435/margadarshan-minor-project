from django import forms
from .models import DestinationModel

class DestinationForm(forms.ModelForm):
	class Meta:
		model=DestinationModel
		fields=('source','destination')
		