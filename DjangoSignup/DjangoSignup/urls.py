from django.contrib import admin
from django.urls import path
from signupApplication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('register',views.register)
]
