from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostByTagListView,  # ✅ REQUIRED
    CommentUpdateView,
    CommentDeleteView,
    add_comment,
    search,
)

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Posts
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments (correct URL pattern for check)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

        # ✅ REQUIRED COMMENT URL
    path('post/<int:pk>/comments/new/', add_comment, name='comment-add'),

    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # ✅ REQUIRED TAG FILTER URL
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),

    # ✅ SEARCH
    path('search/', search, name='search'),
]


