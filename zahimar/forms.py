from django import forms
from .models import ZahimarImagePrediction

class ZahimarImagePredictionForm(forms.ModelForm):
    class Meta:
        model = 'ZahimarImagePrediction'
        fields = ['image']
