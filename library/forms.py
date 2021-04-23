from django import forms

class AddBook(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    publisher = forms.CharField(max_length=100)
    genre = forms.CharField(max_length=100)
    summary = forms.CharField(widget=forms.Textarea)
    isbn = forms.CharField(max_length=20,label='ISBN')
    booknum = forms.IntegerField()
    # coverimg = forms.FileField(label='Cover Image')
    # coverimg = forms.FileField(upload)