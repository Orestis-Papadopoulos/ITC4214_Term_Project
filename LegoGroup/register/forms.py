from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from catalog.models import UserProfile

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100)
    # password field is automatically generated ???

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]

class PasswordChangeForm():
    pass
