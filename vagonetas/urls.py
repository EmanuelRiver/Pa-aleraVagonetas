from django.contrib import admin
from django.urls import path ,include
from vagonetas import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio),
   

]
