from django.contrib import admin
from .models import Category, Subcategory, LegoPart, UserProfile

# username: orestis
# password: admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')

# register your models here (see how you can iterate all classes in models.py instead of doing the following)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(LegoPart)
admin.site.register(UserProfile, UserProfileAdmin)
