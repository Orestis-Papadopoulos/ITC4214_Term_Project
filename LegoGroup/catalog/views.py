from django.shortcuts import render, redirect
from .models import*
from django.views import generic
from .forms import SearchForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def search(request):
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

class SearchResultsListView(generic.ListView):
    model = LegoPart

    def get_queryset(self):
        search_by = self.request.GET.get('search_by')
        search_string = self.request.GET.get('search_string')     
        # https://learndjango.com/tutorials/django-search-tutorial      
        if search_by == 2:
            return LegoPart.objects.filter(category = Category.objects.filter(name__icontains = search_string)) # does not work
        elif search_by == 3:
            return LegoPart.objects.filter(subcategory__name__icontains = 'Gear') # does not work

        return LegoPart.objects.filter(name__icontains = search_string)

# end of ListViews

class LegoPartDetailView(generic.DetailView):
    model = LegoPart
