from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloview(request):
    return render(request,"viewcar.html")