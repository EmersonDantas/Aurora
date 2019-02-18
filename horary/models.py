from django.db import models
from academic import models as academic_models
# Create your models here.

class Horary(models.Model):
    initials = models.CharField(max_length=10)
    hourStart = models.CharField(max_length=5)
    hourEnd = models.CharField(max_length=5)
    classroom = models.CharField(max_length=10)
    subject = models.OneToOneField(academic_models.Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.initials