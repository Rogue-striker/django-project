from django.urls import path

from . import views 

urlpatterns = [
   path('', views.indexpage, name='hello'),
    path('views/',views.indexpage ,name = 'index'),
    path('additem/',views.additem ,name = "adding_list"),
    path('deleteitem/<int:todo_id>/',views.deleteitem,name="deleteitem"),
   
]