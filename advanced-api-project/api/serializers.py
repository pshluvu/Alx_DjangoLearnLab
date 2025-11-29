from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


"""
BookSerializer:
Serializes all fields in the Book model.
Includes custom validation to prevent future publication years.
"""
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        """
        Ensures publication year is not in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


"""
AuthorSerializer:
Serializes the Author model.
Includes a nested BookSerializer to dynamically show related books.
"""
class AuthorSerializer(serializers.ModelSerializer):
    
    # Nested serializer to show all books written by the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
