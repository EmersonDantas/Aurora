from django import forms
from .models import Note, Subject, Period

class NoteForm(forms.Form):
    name = models.CharField(max_length=20)
    weight = models.IntegerField(default=1)
    value = models.DecimalField(max_digits=4, decimal_places=2)

class SubjectForm(forms.Form):
    name = models.CharField(max_length=50)
    credits = models.IntegerField(default=0)

class PeriodForm(forms.Form):
    year = models.CharField(max_length=6)
    cre = models.DecimalField(max_digits=4, decimal_places=2)