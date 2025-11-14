from django.contrib import admin
from .models import Book
from django.contrib.auth import get_user_model

User = get_user_model()  # ensures we use CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'owner')
    list_filter = ('publication_year', 'owner')
    search_fields = ('title', 'author', 'owner__email')
    autocomplete_fields = ('owner',)  # makes selecting users easier

admin.site.register(Book, BookAdmin)
