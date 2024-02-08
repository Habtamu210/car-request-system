from django.contrib import admin
from django.urls import path,include
from .views import helloview,addCarView


urlpatterns = [
    path("",helloview),
    path("add-car/",addCarView),
    
]