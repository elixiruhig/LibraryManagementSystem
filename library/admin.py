from django.contrib import admin

# Register your models here.
from library.models import Book, Category, UserProfile, Inventory

class book_admin(admin.ModelAdmin):
   list_display = ('name', 'author', 'category', 'quantity')
   search_fields = ('name', 'author', 'category', 'quantity')
   list_filter = ('name', 'author', 'category', 'quantity')
admin.site.register(Book, book_admin)

class inventory_admin(admin.ModelAdmin):
   list_display = ('order_id', 'user', 'book', 'status')
   search_fields = ('order_id', 'user', 'book', 'status')
   list_filter = ('order_id', 'user', 'book', 'status')
admin.site.register(Inventory, inventory_admin)


admin.site.register(Category)
admin.site.register(UserProfile)
