from django.shortcuts import render
from django.http import HttpResponse

from .models import Car

# Create your views here.
def helloview(request):
    return render(request,"viewcar.html")

def addCarView(request):
    if request.method=="POST":
        t=request.POST["types"]
        s=request.POST["size"]
        car=Car()
        car.types=t
        car.size=s
        car.save()
        return HttpResponse('/add-book')
        
    return render(request,"addcar.html")