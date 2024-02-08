from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import Car

# Create your views here.
def helloview(request):
    cars=Car.objects.all()
    return render(request,"viewcar.html",{"cars":cars})

def addCarView(request):
    
    return render(request,"addcar.html")

def addCar(request):
    if request.method=="POST":
        t=request.POST["types"]
        s=request.POST["size"]
        print(t,s)
        car=Car()
        car.types=t
        car.size=s
        car.save()
        return HttpResponseRedirect('/')
        
