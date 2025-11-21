# BookViewSet uses TokenAuthentication and requires the user to be authenticated.
# Permission classes ensure that only logged-in users with valid tokens
# can create, update, retrieve, or delete Book records.

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .models import Book
from .serializers import BookSerializer
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer




class BookList(generics.ListAPIView):
    """
    List all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    
class BookViewSet(ModelViewSet):
    """
    A ViewSet for CRUD operations on the Book model.
    Only authenticated users can access these endpoints.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    
    
class BookViewSet(viewsets.ModelViewSet):
    """
    CRUD ViewSet for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]






# Create your views here.
