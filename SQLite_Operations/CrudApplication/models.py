from django.db import models

class data(models.Model):#data is our class name
    UserName=models.CharField(max_length=20,default="")
    Password=models.CharField(max_length=20,default="")

    
