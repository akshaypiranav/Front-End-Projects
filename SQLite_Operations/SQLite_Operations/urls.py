from django.contrib import admin
from django.urls import path
from CrudApplication import views
urlpatterns = [
    path('admin',admin.site.urls),
    path('',views.home,name='home'),
    path('addDetails',views.addDetails,name='addDetails'),
    path('updateData/<int:id>',views.updateData,name='updateData'),
    path('deleteData/<int:id>',views.deleteData,name='deleteData')
    
]
