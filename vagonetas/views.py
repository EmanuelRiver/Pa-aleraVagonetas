from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request,"vagonetas/inicio.html")
   

def pañales(request):
    return render(request,"vagonetas/pañales.html")

def indumentaria(request):
    return render(request,"vagonetas/indumentaria.html")

def perfumeria(request):
    return render(request,"vagonetas/perfumeria.html")

def accesorios(request):
    return render(request,"vagonetas/accesorios.html")