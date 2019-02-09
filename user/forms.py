from django import forms
from .models import User, Student

SEX_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

class UserForm(forms.Form):
    first_name = forms.CharField(label="Primeiro nome", max_length=20)
    last_name = forms.CharField(label="Ultimo nome", max_length=20)
    email = forms.EmailField(label="Email", max_length=30)
    password = forms.CharField(label="Senha", max_length=12, widget=forms.PasswordInput)
    birth_date = forms.DateField(label="Data de Nascimento")
    sex = forms.ChoiceField(label="Sexo", choices = SEX_CHOICES)
    profile_photo = forms.ImageField(label="Foto de perfil")



class StudentForm(UserForm):
    ies = forms.CharField(label="Universidade", max_length=50)
    course = forms.CharField(label="Curso", max_length=50)
    