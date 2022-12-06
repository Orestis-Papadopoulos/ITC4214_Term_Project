from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/catalog/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'templates/registration/login.html', context = {'form': form})
    