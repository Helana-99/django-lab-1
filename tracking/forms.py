from django import forms
from .models import Tracking

class TrackingForm(forms.ModelForm):
    class Meta:
        model = Tracking
        fields = ['trainee', 'progress', 'date']
