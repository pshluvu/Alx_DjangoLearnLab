from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=200, required=False, label='Search Books')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
