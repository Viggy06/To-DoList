from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
  path('',views.register, name='register'),
#when request come it verifies name then path and views
  #you can give 'anythng here/' <- but name and views.method name should be same
  path('login/',views.loginuser, name="loginuser"),
  path('logout/',views.logoutuser, name="logoutuser"),
  path('home/',views.home, name="home"),
  
  #create todo
  path('createtodo/',views.createtodo, name="createtodo"),
  path('currenttodo/',views.currenttodos, name="currenttodos"), 
  path('completed/',views.completedtodo, name="completedtodos"), 
  path('todo/<int:todo_pk>',views.viewtodo, name="viewtodo"),
  path('todo/<int:todo_pk>/complete',views.completetodo, name="completetodo"),
  path('todo/<int:todo_pk>/deletetodo',views.deletetodo, name="deletetodo"),
]
