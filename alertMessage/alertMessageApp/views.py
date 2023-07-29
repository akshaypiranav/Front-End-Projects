from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home.html')

def success(request):
    messages.success(request,"ALERT MESSAGE IS SUCCESS")
    return render(request,'home.html')

def info(request):
    messages.info(request,"ALERT MESSAGE IS INFO")
    return render(request,'home.html')
def error(request):
    messages.error(request,"ALERT MESSAGE IS ERROR")
    return render(request,'home.html')
def warning(request):
    messages.warning(request,"ALERT MESSAGE IS WARNING")
    return render(request,'home.html')

