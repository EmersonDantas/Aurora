from django.db import models

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=20)
    weight = models.IntegerField(default=1)
    value = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        return self.name + ": " + str(self.value)

class Subject(models.Model):
    name = models.CharField(max_length=50)
    credits = models.IntegerField(default=0)
    notes = models.ForeignKey(Note, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name

class Period(models.Model):
    year = models.CharField(max_length=6)
    subjects = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True, blank=True)
    cre = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.year)
