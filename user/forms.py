from django.forms import ModelForm
from .models import User, Student

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birth_date', 'sex', 'profile_photo']



class StudentForm(UserForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'birth_date', 'sex', 'profile_photo', 'ies', 'course', 'year_graduation']
    