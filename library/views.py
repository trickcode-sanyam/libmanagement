from django.shortcuts import render,redirect
from .models import Book, Request, Review, ReviewWarning
from django.contrib.auth.models import User
from .forms import AddBook, AddRequest, AddReview
from django.contrib import messages
from datetime import date

def home(request):
    allbooks = Book.objects.all().reverse()
    l = len(allbooks)
    if l < 10:
        return render(request, 'home.html',{'curruser': request.user, 'books': allbooks})
    else:
        return render(request, 'home.html',{'curruser': request.user, 'books': allbooks[(l-10):]})


def book(request,bknum):
    bookSet = Book.objects.filter(booknum = bknum)
    if len(bookSet) == 0:
        messages.warning(request,'No book found with number '+str(bknum))  
        return redirect('/')
    elif len(bookSet) > 1:
        messages.warning(request,'More than 1 book found with number '+str(bknum))  
        return redirect('/')
    else:
        book = bookSet[0]
        if request.method == 'POST':
            user = request.user
            if not request.POST.get('addrequest') == None:
                gotrequest = AddRequest(request.POST)
                if gotrequest.is_valid():            
                    fromdate = request.POST.get('fromdate')
                    todate = request.POST.get('todate')
                    if fromdate < todate and fromdate >= str(date.today()):
                        newrequest = Request(user = user, book = book, fromdate = fromdate, todate = todate, seen=False, accepted = False)
                        newrequest.save()
                        messages.success(request, 'Request sent successfully!')
            elif not request.POST.get('warnreview') == None:
                reviewid = request.POST.get('reviewid')
                Review.objects.get(id=reviewid).delete()
                book = Book.objects.get(id=request.POST.get('bookid'))
                user = User.objects.get(id=request.POST.get('userid'))
                newwarning = ReviewWarning(book=book,user=user)
                newwarning.save()
            else:
                gotreview = AddReview(request.POST)
                if gotreview.is_valid():  
                    rating = request.POST.get('rating')
                    review = request.POST.get('review')
                    newreview = Review(rating = rating, review = review, user = user, book = book)
                    newreview.save()
                    messages.success(request, 'Review added successfully!')
                else:
                    messages.warning(request, "Couldn't add review!")
        reviewset = reversed(Review.objects.filter(book=book))
        if request.user.is_authenticated:
            if request.user.profile.isLibrarian:
                requestset = reversed(Request.objects.filter(book=book))
            else: requestset = 'blank'
        else:
            requestset = 'blank'
        return render(request, 'book.html', {'book': book,'curruser': request.user,'form': AddRequest, 'reviewform': AddReview, 'reviews': reviewset, 'requests': requestset})

def addbook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        publisher = request.POST.get('publisher')
        genre = request.POST.get('genre')
        summary = request.POST.get('summary')
        isbn = request.POST.get('isbn')
        booknum = request.POST.get('booknum')
        isavl = request.POST.get('avl')
        coverimg = request.FILES.get('coverimg')
        if not isavl == None:
            avl = True
        else:
            avl = False        
        newbook = Book(title=title, author=author, publisher=publisher, genre=genre, summary=summary, isbn=isbn, avl=avl, booknum=booknum, coverimg= coverimg)
        newbook.save()
        messages.success(request, 'Book added successfully!')
        # handle_uploaded_file(request.FILES['coverimg'],str(booknum))
    return render(request, 'addbook.html',{'curruser': request.user, 'form': AddBook})

# def handle_uploaded_file(f, bknum):
#     with open('static/bookcovers/' + bknum + '.jpg', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def editbook(request,bknum):
    bookSet = Book.objects.filter(booknum = bknum)
    if len(bookSet) == 0:
        messages.warning(request,'No book found with number '+str(bknum))  
        return redirect('/')
    elif len(bookSet) > 1:
        messages.warning(request,'More than 1 book found with number '+str(bknum))  
        return redirect('/')
    else:
        book = bookSet[0]
        if request.method=='POST':
            if not request.POST.get('save') == None:
                book.title = request.POST.get('title')
                book.author = request.POST.get('author')
                book.publisher = request.POST.get('publisher')
                book.genre = request.POST.get('genre')
                book.summary = request.POST.get('summary')
                book.isbn = request.POST.get('isbn')
                book.booknum = request.POST.get('booknum')
                isavl = request.POST.get('avl')
                if not isavl == None:
                    book.avl = True
                else:
                    book.avl = False
                book.save()
                messages.success(request, "Book details updated successfully! Click on 'Done Editing' to go back.")
                form = AddBook(initial=
                    {'title': book.title,
                    'author': book.author,
                    'publisher': book.publisher,
                    'summary': book.summary,
                    'genre': book.genre,
                    'isbn': book.isbn,
                    'avl': book.avl,
                    'booknum': book.booknum,}
                )
                return render(request, 'editbook.html',{'curruser': request.user, 'form': form, 'book': book})
            else:
                book.delete()
                messages.success(request, 'Book deleted successfully')
                return redirect('/')
        else:
            form = AddBook(initial=
                {'title': book.title,
                'author': book.author,
                'publisher': book.publisher,
                'summary': book.summary,
                'genre': book.genre,
                'isbn': book.isbn,
                'booknum': book.booknum,}
            )            
        return render(request, 'editbook.html',{'curruser': request.user, 'form': form, 'book': book})


def search(request):
    if request.method=='POST':
        searchquery = request.POST.get('query').strip()
        if not searchquery == '':
            queryintitle = Book.objects.filter(title__contains=searchquery)
            queryinauthor = Book.objects.filter(author__contains=searchquery)
            queryinsummary = Book.objects.filter(summary__contains=searchquery)
            queryinpublisher = Book.objects.filter(publisher__contains=searchquery)
            return render(request, 'searchresults.html', {'curruser': request.user , 'queryintitle': queryintitle, 'queryinauthor': queryinauthor, 'queryinsummary': queryinsummary, 'queryinpublisher': queryinpublisher, 'searchquery': searchquery})
    return redirect('/')

def author(request,authorname):
    queryinauthor = Book.objects.filter(author=authorname)
    return render(request, 'author.html', {'curruser': request.user , 'queryinauthor': queryinauthor, 'authorname': authorname})

def genre(request,genrename):
    queryingenre = Book.objects.filter(genre=genrename)
    return render(request, 'genre.html', {'curruser': request.user , 'queryingenre': queryingenre, 'genrename': genrename})