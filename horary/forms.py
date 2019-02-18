from django import forms
from .models import Horary

class HoraryForm(forms.Form):
    initials = models.CharField(max_length=10)
    hourStart = models.CharField(max_length=5)
    hourEnd = models.CharField(max_length=5)
    classroom = models.CharField(max_length=10)