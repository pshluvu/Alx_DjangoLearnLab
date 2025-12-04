from rest_framework import generics, permissions
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets



# --- Book ViewSet (Handles all CRUD operations and filtering) ---
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing book instances.
    This replaces separate ListAPIView, CreateAPIView, etc., making all methods available.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # Allow read access to anyone, but require authentication for write/update/delete.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] 

    # Filtering/Searching/Ordering Configuration
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name'] # Allows searching books by title or author name
    ordering_fields = ['publication_year', 'title'] # Allows ordering by year or title


# --- Author ViewSet ---
class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A ViewSet for viewing author instances (Read-Only).
    We use ReadOnlyModelViewSet because nested serializers often make writes complicated.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]





class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


"""
BookListView:
Handles retrieving all Book records.
Read-only access for unauthenticated users.
"""
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public read access




class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



"""
BookDetailView:
Handles retrieving a single Book by ID.
Read-only access for unauthenticated users.
"""
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public read access


"""
BookCreateView:
Handles creation of new Book records.
Only authenticated users are allowed.
"""
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom hook to control how objects are saved.
        Ensures validation runs before saving.
        """
        serializer.save()


"""
BookUpdateView:
Handles updating existing Book records.
Only authenticated users are allowed.
"""
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Custom hook for update logic.
        """
        serializer.save()


"""
BookDeleteView:
Handles deleting Book records.
Only authenticated users are allowed.
"""
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # ✅ Enable filtering, searching, and ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # ✅ Filtering fields
    filterset_fields = ['title', 'publication_year', 'author']

    # ✅ Search fields (text search)
    search_fields = ['title', 'author__name']

    # ✅ Ordering fields
    ordering_fields = ['title', 'publication_year']

    # ✅ Default ordering
    ordering = ['title']
