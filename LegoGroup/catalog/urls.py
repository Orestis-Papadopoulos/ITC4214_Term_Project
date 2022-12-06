from django.urls import path
from . import views # views are in this directory
from django.contrib import admin

# the parameter 'name' is used to reference a URL in a template
urlpatterns = [
    path('', views.index, name = 'index'),
    path('lego_parts/', views.LegoPartListView.as_view(), name = 'lego_parts'),
    path('about/', views.about, name = 'about'),
]
