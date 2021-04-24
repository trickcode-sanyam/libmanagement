from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
class AddBook(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    publisher = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=100)
    summary = forms.CharField(widget=forms.Textarea)
    isbn = forms.CharField(max_length=20,label='ISBN')
    booknum = forms.IntegerField()
    avl = forms.BooleanField(label='Available',initial=True,required=False)
    # coverimg = forms.FileField(label='Cover Image')
    # coverimg = forms.FileField(upload)

class DateInput(forms.DateInput):
    input_type = 'date' #default is text

class AddRequest(forms.Form):
    fromdate = forms.DateField(label='From',widget=DateInput)
    todate = forms.DateField(label='To',widget=DateInput)

class AddReview(forms.Form):
    rating = forms.IntegerField(label='Rating (1-5)',validators=[MaxValueValidator(5),MinValueValidator(1)])
    review = forms.CharField(widget=forms.Textarea(attrs={'rows':4}), label='Review')