from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label = 'AAAAhh', max_length = 100)
    password = forms.CharField(label = 'Password', max_length = 100)