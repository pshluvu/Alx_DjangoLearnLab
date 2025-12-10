from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostByTagListView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
    add_comment,
    search,
    TagListView,
)

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Posts
    path('', PostListView.as_view(), name='post-list'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('posts/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('posts/<int:pk>/comments/add/', add_comment, name='comment-add'),

    # Tags
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
    path('tags/<str:tag_name>/', TagListView.as_view(), name='posts-by-tag-alt'),

    # Search
    path('search/', search, name='search'),
]




