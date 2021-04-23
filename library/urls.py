from django.urls import path,include
from library import views

urlpatterns = [
    path('', views.home, name="home"),
    path('book/<int:bknum>', views.book, name='book'),
    path('addbook', views.addbook, name='addbook')
]