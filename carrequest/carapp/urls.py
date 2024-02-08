from django.contrib import admin
from django.urls import path,include,re_path
from .views import helloview,addCarView,addCar


urlpatterns = [
    path("",helloview),
    path("add-car/",addCarView),
    re_path("add-car/add",addCar),
    
]