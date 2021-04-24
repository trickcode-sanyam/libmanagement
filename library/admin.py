from django.contrib import admin
from .models import Book, Request, Review

admin.site.register(Book)
admin.site.register(Request)
admin.site.register(Review)