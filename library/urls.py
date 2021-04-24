from django.urls import path,include
from library import views

urlpatterns = [
    path('', views.home, name="home"),
    path('book/<int:bknum>', views.book, name='book'),
    path('addbook', views.addbook, name='addbook'),
    path('book/<int:bknum>/edit', views.editbook, name='editbook'),
    path('author/<str:authorname>', views.author, name='author'),
    path('genre/<str:genrename>', views.genre, name='genre'),
    path('search', views.search , name = 'search')
]