from django.contrib import admin
from .models import Book, Request, Review, ReviewWarning

admin.site.register(Book)
admin.site.register(Request)
admin.site.register(Review)
admin.site.register(ReviewWarning)