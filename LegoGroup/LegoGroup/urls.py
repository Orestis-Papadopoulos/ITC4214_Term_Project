"""LegoGroup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from register import views as rv
from catalog import views as cv

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),

    # forward requests starting with 'catalog/' to the catalog.urls module
    # every URL in the 'catalog' app will be prefixed with 'catalog/' ??? isn't that what the lext command does ???
    path('catalog/', include('catalog.urls')),

    # redirect the root URL 127.0.0.1:8000 to the URL 127.0.0.1:8000/catalog/
    path('', RedirectView.as_view(url = 'catalog/', permanent = True)),

    # site authentication urls
    path('accounts/', include('django.contrib.auth.urls')),

    path('register/', rv.register, name = 'register'),
    path('', include('django.contrib.auth.urls')), # what does this do ???

    path('accounts/login/', rv.login, name = 'login'),

    path('search/', cv.search, name = 'search'),
    path('search_anonymous/', cv.search_anonymous, name = 'search_anonymous'),

    path('update_account/', rv.update_account, name = 'update_account'),

    path('password/', rv.change_password, name = 'change_password')

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
