from django.shortcuts import render
from .models import*
from django.views import generic

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class LegoPartListView(generic.ListView):
    model = LegoPart

    user_input = ''

    search_by_name = True
    search_by_category = False
    search_by_subcategory = False
    
    if (search_by_name): queryset = LegoPart.objects.filter(name__icontains = user_input)
    elif (search_by_category): queryset = LegoPart.objects.filter(category__icontains = user_input)
    elif (search_by_subcategory): queryset = LegoPart.objects.filter(subcategory__icontains = user_input)
