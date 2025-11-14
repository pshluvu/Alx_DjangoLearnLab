from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Data Setup (Run once if needed) ---
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

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    books = Book.objects.filter(author__name=author_name)
    return books


def list_books_in_library(library_name):
    """List all books in a library."""
    library = Library.objects.get(name=library_name)
    return library.books.all()


def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    library = Library.objects.get(name=library_name)
    return library.librarian


# --- Example Usage (for testing in Django shell) ---
if __name__ == "__main__":
    # Run this with: python manage.py shell < relationship_app/query_samples.py

    setup_sample_data()

    print("\nBooks by J.K. Rowling:")
    for book in query_books_by_author("J.K. Rowling"):
        print("-", book.title)

    print("\nBooks in Central Library:")
    for book in list_books_in_library("Central Library"):
        print("-", book.title)

    print("\nLibrarian for Community Library:")
    print(get_librarian_for_library("Community Library").name)
