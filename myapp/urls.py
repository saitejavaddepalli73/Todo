from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.Registerpage,name='register'),
    path('insert/',views.insertData, name='insert'),
    path('showpage/',views.showPage, name='show'),
    path('delete/<int:pk>', views.deleteData, name='delete'),
    # path('register/',views.Registerpage, name='register'),
    path('login/',views.LoginPage, name='login'),
    path('register/',views.registerUser, name='registerpage'),
    path('loginuser/',views.userlogin, name='loginuser'),
    path('logout/',views.logoutUser, name='logout'),
    path('update/<int:pk>', views.UpdateData, name='update'),
]