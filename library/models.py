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
    ondate = models.DateField(auto_now_add=True)
    def __str__(self):
        return 'On ' + str(self.ondate) + ' by ' + self.user.username + ' (' + str(self.fromdate) + ' to ' + str(self.todate) + ')'
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    ondate = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.book.booknum) + ' by ' + self.user.username + ': ' + self.review[:20] + '(' + str(self.ondate) + ')'

class ReviewWarning(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    ondate = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.book.booknum) + ' by ' + self.user.username + '(dated ' + str(self.ondate) + ')'
