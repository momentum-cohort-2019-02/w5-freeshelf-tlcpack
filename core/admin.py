from django.contrib import admin
from core.models import Book, Category, Favorite

# Register your models here.
admin.site.register(Book)
admin.site.register(Category)