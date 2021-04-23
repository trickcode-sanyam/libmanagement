from django.db import models

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

    

