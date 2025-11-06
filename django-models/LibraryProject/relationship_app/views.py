from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library


# Create your views here.
def list_books(request):
    books = Book.objects.all()  # Fetch all Book objects from the database
    context = {'books': books}  # Pass data to the template
    return render(request, 'list_books.html', context)
