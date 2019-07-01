from django.contrib import admin

# Register your models here.
from library.models import Book, Category, UserProfile, Inventory

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Inventory)