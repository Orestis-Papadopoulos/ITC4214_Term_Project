from django.shortcuts import render

# home page
def base(request):
    return render(request, "base.html")

def about(request):
    pass

def search_results(request):
    pass

def login(request):
    pass

def create_account(request):
    pass

# redirects to the 'create_account' page where the fields contain the user's info?
def user_profile(request):
    pass
