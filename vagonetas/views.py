from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request,"vagonetas/inicio.html")
   

def pañales(request):
    return render(request,"vagonetas/pañales.html")