from django.shortcuts import render,redirect
from .form import CreateUserForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        name=request.POST.get("username")
        emaill=request.POST.get("email")
        passwordl=request.POST.get("password")
        confirm=request.POST.get("confirm")
        if passwordl==confirm:
            user=User.objects.create_user(username=name,email=emaill,password=passwordl)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            return redirect("login")
        
    
    else:
        # form=CreateUserForm()  inbuilt form for register if want send form in the render
        return render(request,"register.html")