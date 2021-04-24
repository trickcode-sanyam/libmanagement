from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    summary = models.TextField()
    isbn = models.CharField(max_length=20)
    avl = models.BooleanField()
    booknum = models.IntegerField()
    def __str__(self):
        return self.title

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    fromdate = models.DateField(auto_now=False, auto_now_add=False)
    todate = models.DateField(auto_now=False, auto_now_add=False)
    seen = models.BooleanField()
    accepted = models.BooleanField()
    reqname = models.CharField(max_length=200)
    def __str__(self):
        return self.reqname

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    def __str__(self):
        return str(self.book.booknum) + ' by ' + self.user.username + ': ' + self.review[:20]

class ReviewWarning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.book.booknum) + ' by ' + self.user.username
