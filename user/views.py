from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import StudentForm
from django.contrib.auth.models import User as UserD
from .models import User, Student
from django.contrib import messages
from django.db import IntegrityError

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')

def loginUser(request):
    return render(request, 'registration/login.html')

def registerUser(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    
    if(form.is_valid()):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        birth_date = form.cleaned_data['birth_date']
        sex = form.cleaned_data['sex']
        ies = form.cleaned_data['ies']
        course = form.cleaned_data['course']
        profile_photo = request.FILES['profile_photo']

        try:
            #Criando o usuario usando o django auth
            userDjango = UserD.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)
        except IntegrityError:
            return render(request, 'registration/register.html', {'form':form})
        # Criando o usuario Aurora
        myUser = User(user=userDjango, birth_date=birth_date, sex=sex, profile_photo=profile_photo)
        myUser.save_base()

        # Criando um usuario estudante
        student = Student(user=myUser, ies=ies, course=course)
        student.save_base()

        return redirect('home')
    return render(request, 'registration/register.html', {'form':form})