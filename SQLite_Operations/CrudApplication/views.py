from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import data


def home(request):

    myData=data.objects.all()
    if (myData != ''):
        return render(request,'home.html',{'data':myData})
    else:
        return render(request,"home.html")
    
def addDetails(request):
        if(request.method=='POST'):
            name=request.POST['name']
            password=request.POST['password']
            obj=data()
            obj.UserName=name
            obj.Password=password
            obj.save()
            myData=data.objects.all()
            return redirect('home')
        return render(request,'home.html',{'data':myData})
def updateData(request,id):
     myData=data.objects.get(id=id)
     if(request.method=='POST'):
          name=request.POST['name']
          password=request.POST['password']
          myData.UserName=name
          myData.Password=password
          myData.save()
          print("ulla vanthuruchi")
          return redirect('home')

     return render(request,'update.html',{'data':myData})

def deleteData(request,id):
     myData=data.objects.get(id=id)
     myData.delete()
     return redirect('home')