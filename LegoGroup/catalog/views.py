from django.shortcuts import render, redirect
from .models import*
from django.views import generic
from .forms import SearchForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/lego_parts/") # filter queryset here ???
    else:
        form = SearchForm()
    return render(request, 'search.html', {"form": form})

# start of ListViews

class BrickListView(generic.ListView):
    model = LegoPart

    def get_queryset(self):
        return LegoPart.objects.filter(name__icontains = 'Brick')

class TechnicListView(generic.ListView):
    model = LegoPart

    def get_queryset(self):
        return LegoPart.objects.filter(name__icontains = 'Technic')

class ElectricListView(generic.ListView):
    model = LegoPart

    def get_queryset(self):
        return LegoPart.objects.exclude(name__icontains = 'Brick').exclude(name__icontains = 'Technic')

class LegoPartListView(generic.ListView):
    model = LegoPart

    user_input = ''

    search_by_name = True
    search_by_category = False
    search_by_subcategory = False
    
    if (search_by_name): queryset = LegoPart.objects.filter(name__icontains = user_input)
    elif (search_by_category): queryset = LegoPart.objects.filter(category__icontains = user_input)
    elif (search_by_subcategory): queryset = LegoPart.objects.filter(subcategory__icontains = user_input)

# end of ListViews

class LegoPartDetailView(generic.DetailView):
    model = LegoPart
