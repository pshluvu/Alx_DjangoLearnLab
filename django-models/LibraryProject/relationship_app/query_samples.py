from relationship_app.models import Author, Book, Library, Librarian




def setup_sample_data():
    author1 = Author.objects.create(name="J.K. Rowling")
    author2 = Author.objects.create(name="George Orwell")

    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book2)

    library2 = Library.objects.create(name="Community Library")
    library2.books.add(book3)

    librarian1 = Librarian.objects.create(name="Alice", library=library1)
    librarian2 = Librarian.objects.create(name="Bob", library=library2)

    print("Sample data created successfully.")


# --- Queries ---
#Add advanced_features_and_security directory

# Query all books by a specific author
def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    
    books = Book.objects.filter(author=author)
    return books


# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

