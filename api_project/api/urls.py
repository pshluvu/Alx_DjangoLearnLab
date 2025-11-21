from django.urls import path
from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from .views import BookList
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import BookViewSet


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),

    # Token authentication endpoint
    path('token/', obtain_auth_token, name='api-token'),

    path('', include(router.urls)),
]


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),  # Include all CRUD endpoints
]