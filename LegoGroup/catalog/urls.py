from django.urls import path
from . import views # views are in this directory

urlpatterns = [
    path('', views.index, name = "index"),
    path('lego_parts/', views.LegoPartListView.as_view(), name = 'lego_parts'),
    path('about/', views.about, name = 'about')
]
