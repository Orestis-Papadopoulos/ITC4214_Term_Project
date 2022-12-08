from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, UserChangeForm, EditProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

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
            form.save()
        
    return render(request, 'templates/registration/login.html', context = {'form': form})

@login_required
def update_account(request):
    # form = UserChangeForm(instance = request.user) # the default form
    form = EditProfileForm(instance = request.user) # customized to not show all user info
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()

    return render(request, 'register/update_account.html', context = {'form': form})

@login_required
def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            #return redirect('update_account/') # does not work
    
    return render(request, 'register/change_password.html', context = {'form': form})
