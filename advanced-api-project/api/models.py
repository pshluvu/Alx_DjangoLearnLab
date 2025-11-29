from django.db import models

"""
Author model:
Represents a book author.
Each author can have multiple books (one-to-many relationship).
"""
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


"""
Book model:
Represents a book written by an author.
Each book belongs to one author through a ForeignKey relationship.
"""
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    
    # Establishes one-to-many relationship: One Author → Many Books
    author = models.ForeignKey(
        Author,
        related_name="books",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


# Create your models here.
