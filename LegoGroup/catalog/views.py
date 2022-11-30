from django.shortcuts import render
from .models import *
from django.views import generic

"""
def base(request):
    return render(request, 'base.html')
"""

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

""" this is implemented as a class-based view
def lego_parts(request):
    lego_parts_count = LegoPart.objects.count() # .all() is implied by default

    context = {
        'lego_parts_count': lego_parts_count
    }

    return render(request, 'lego_parts.html', context = context)
"""

def login(request):
    pass

def create_account(request):
    pass

# redirects to the 'create_account' page where the fields contain the user's info?
def user_profile(request):
    pass

class LegoPartListView(generic.ListView):
    model = LegoPart

    user_input = ''

    search_by_name = True
    search_by_category = False
    search_by_subcategory = False
    
    if (search_by_name): queryset = LegoPart.objects.filter(name__icontains = user_input)
    elif (search_by_category): queryset = LegoPart.objects.filter(category__icontains = user_input)
    elif (search_by_subcategory): queryset = LegoPart.objects.filter(subcategory__icontains = user_input)
