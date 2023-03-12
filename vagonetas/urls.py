from django.contrib import admin
from django.urls import path ,include
from vagonetas import views
urlpatterns = [
    path('', views.Inicio,name='Inicio'),
    path('pañales',views.pañales,name='Pañales'),
   

]
