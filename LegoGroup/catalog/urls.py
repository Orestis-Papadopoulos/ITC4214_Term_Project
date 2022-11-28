from django.urls import path
from . import views # views are in this directory

urlpatterns = [
    path('', views.base, name = "base")
]
