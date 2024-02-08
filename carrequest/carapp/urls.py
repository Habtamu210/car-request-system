from django.contrib import admin
from django.urls import path,include
from .views import helloview


urlpatterns = [
    path("",helloview)
    
]