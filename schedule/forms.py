from django import forms
from .models import Note, Subject, Period

class NoteForm(forms.Form):
    name = forms.CharField(max_length=20)
    weight = forms.IntegerField()
    value = forms.DecimalField(max_digits=4, decimal_places=2)

class SubjectForm(forms.Form):
    name = forms.CharField(max_length=50)
    credits = forms.IntegerField()

class PeriodForm(forms.Form):
    year = forms.CharField(max_length=6)