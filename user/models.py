from django.db import models
from django.contrib.auth.models import User as UserD

SEX_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

class User(models.Model): # User Aurora
    user = models.OneToOneField(UserD, related_name="user", on_delete="CASCADE") # User Django
    birth_date = models.DateField(max_length=10)
    sex = models.CharField(max_length=1, choices = SEX_CHOICES)
    profile_photo = models.ImageField(upload_to="profile_photos", null=True, blank = True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Student(models.Model): # Student Aurora
    user = models.OneToOneField(User, related_name="student", on_delete="CASCADE") # User Aurora
    ies = models.CharField(max_length=50)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.user.user.first_name + ' ' + self.user.user.last_name