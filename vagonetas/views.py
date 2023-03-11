from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request,"pañalera_vagonetas/inicio.html")
    #return HttpResponse("Vista inicio")