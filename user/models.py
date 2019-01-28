from django.db import models

SEX_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    sex = models.CharField(max_length=1, choices = SEX_CHOICES)
    profile_photo = models.ImageField(upload_to="profile_photos", null=True, blank = True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Student(User):
    ies = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    year_graduation = models.IntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name