from django.db import models
from user import models as user_models

# Create your models here.
class Period(models.Model):
    year = models.CharField(max_length=6)
    cre = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=True)
    student = models.ForeignKey(user_models.Student, on_delete=models.PROTECT , null=True, blank=True)

    def __str__(self):
        return str(self.year)

class Subject(models.Model):
    name = models.CharField(max_length=50)
    credits = models.IntegerField(default=0)
    period = models.ForeignKey(Period, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(user_models.Student, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Note(models.Model):
    name = models.CharField(max_length=20)
    weight = models.IntegerField(default=1)
    value = models.DecimalField(max_digits=4, decimal_places=2)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    period = period = models.ForeignKey(Period, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name + ": " + str(self.value)

