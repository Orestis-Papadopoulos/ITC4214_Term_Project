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
    pass

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
