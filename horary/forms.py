from django import forms
from .models import Horary

class HoraryForm(forms.Form):
    initials = forms.CharField(max_length=10)
    hourStart = forms.CharField(max_length=5)
    hourEnd = forms.CharField(max_length=5)
    classroom = forms.CharField(max_length=10)