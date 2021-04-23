from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.models import User
from .forms import AddBook
def home(request):
    return render(request, 'home.html',{'curruser': request.user})

def book(request,bknum):
    bookSet = Book.objects.filter(booknum = bknum)
    if len(bookSet) == 0:
        return HttpResponse("No such book exists")       
    elif len(bookSet) > 1:
        return HttpResponse("More than 1 book with same number exist")
    else: 
        return render(request, 'book.html', {'book': bookSet[0],'curruser': request.user})

def addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        genre = request.POST.get('genre')
        summary = request.POST.get('summary')
        isbn = request.POST.get('isbn')
        booknum = request.POST.get('booknum')
        newbook = Book(title=title, author=author, publisher=publisher, genre=genre, summary=summary, isbn=isbn, avl=True, booknum=booknum)
        newbook.save()
        # handle_uploaded_file(request.FILES['coverimg'],str(booknum))
    return render(request, 'addbook.html',{'curruser': request.user, 'form': AddBook})

# def handle_uploaded_file(f, bknum):
#     with open('static/bookcovers/' + bknum + '.jpg', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)