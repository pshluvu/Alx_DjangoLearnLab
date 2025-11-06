# Django Admin Configuration for Book Model

## Admin Registration
Registered the Book model in `bookshelf/admin.py` using `@admin.register(Book)`.

## Custom Display
- Fields shown: `title`, `author`, `publication_year`
- Filters: `author`, `publication_year`
- Searchable fields: `title`, `author`

## Access Instructions
- Run: `python manage.py runserver`
- Visit: `http://127.0.0.1:8000/admin`
- Log in with superuser credentials