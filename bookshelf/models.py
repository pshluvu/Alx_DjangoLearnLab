from django.db import models
from django.conf import settings  # <-- import settings for custom user

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    # Add a ForeignKey to the custom user model
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'  # optional, makes reverse lookup easy
    )

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
