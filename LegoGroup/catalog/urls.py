from django.urls import path
from . import views # views are in this directory
from django.contrib import admin

# the parameter 'name' is used to reference a URL in a template
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),

    # for the ListViews
    path('lego_parts/', views.LegoPartListView.as_view(), name = 'lego_parts'),
    path('bricks/', views.BrickListView.as_view(), name = 'bricks'),
    path('technics/', views.TechnicListView.as_view(), name = 'technics'),
    path('electrics/', views.ElectricListView.as_view(), name = 'electrics'),
    path('search_results/', views.SearchResultsListView.as_view(), name = 'search_results'),

    # for the detail views
    path('lego_parts/<pk>/', views.LegoPartDetailView.as_view(), name = 'legopart-detail'),
    path('bricks/<pk>/', views.LegoPartDetailView.as_view(), name = 'legopart-detail'),
    path('technics/<pk>/', views.LegoPartDetailView.as_view(), name = 'legopart-detail'),
    path('electrics/<pk>/', views.LegoPartDetailView.as_view(), name = 'legopart-detail'),
]
