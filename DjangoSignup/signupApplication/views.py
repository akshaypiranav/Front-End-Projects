from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    name=request.POST['name']
    address=request.POST['address']
    mail=request.POST['mail']
    password=request.POST['password']
    return render(request,'output.html',{'NAME':name,'PASSWORD':password,'MAIL':mail,'ADDRESS':address})
