from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'list_books.html', context)


# Class-based view: display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
