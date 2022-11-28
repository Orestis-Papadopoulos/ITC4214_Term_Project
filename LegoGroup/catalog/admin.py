from django.contrib import admin
from .models import Category, Subcategory, LegoPart, User

# username: orestis
# password: admin

# register your models here (see how you can iterate all classes in models.py instead of doing the following)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(LegoPart)
admin.site.register(User)
