from django.contrib import admin
from django.urls import path ,include
from vagonetas import views
urlpatterns = [
    path('', views.Inicio,name='Inicio'),
    path('pañales',views.pañales,name='Pañales'),
    path('indumentaria',views.indumentaria,name='Indumentaria'),
    path('perfumeria',views.perfumeria,name='Perfumeria'),
    path('accesorios',views.accesorios,name='Accesorios'),
   

]
