# Advanced API Project – Book CRUD with Django REST Framework

## Implemented Views

| Endpoint | Method | Description | Permission |
|----------|--------|-------------|------------|
| /api/books/ | GET | List all books | Public |
| /api/books/<id>/ | GET | Retrieve single book | Public |
| /api/books/create/ | POST | Create book | Auth only |
| /api/books/<id>/update/ | PUT | Update book | Auth only |
| /api/books/<id>/delete/ | DELETE | Delete book | Auth only |

## Permissions
- Read operations: Open to all users
- Write operations: Restricted to authenticated users using DRF IsAuthenticated

## Custom Behavior
- Validation prevents future publication years
- Custom perform_create and perform_update hooks ensure controlled saves
- Nested serialization of books inside authors

## Technologies
- Django
- Django REST Framework
- SQLite


## Filtering, Searching & Ordering – Book API

### Filtering
Filter books by:
- title
- publication_year
- author (author ID)

#### Example:
GET /api/books/?publication_year=2023  
GET /api/books/?author=1  

---

### Searching
Search is enabled on:
- Book title
- Author name

#### Example:
GET /api/books/?search=django  
GET /api/books/?search=ndlovu  

---

### Ordering
Ordering is enabled on:
- title
- publication_year

#### Example:
GET /api/books/?ordering=title  
GET /api/books/?ordering=-publication_year  

---

### Combined Query Example
GET /api/books/?author=1&search=python&ordering=-publication_year
