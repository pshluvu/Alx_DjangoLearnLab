from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView route
    path('books/', BookList.as_view(), name='book-list'),

    # Router-generated CRUD routes
    path('', include(router.urls)),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),   # Connects to the api app
]
