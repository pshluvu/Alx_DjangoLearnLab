from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    ExampleForm for creating or updating Book instances.
    Includes basic validation and CSRF protection when used in templates.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
            'publication_year': forms.NumberInput(attrs={'placeholder': 'Enter year'}),
        }
