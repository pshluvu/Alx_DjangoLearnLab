from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    # =========================
    # AUTHENTICATION URLs
    # =========================
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    # You can add Django's built-in login/logout views if needed:
    # path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),

    # =========================
    # BLOG POST URLs
    # =========================
    path('', PostListView.as_view(), name='post-list'),                     # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),   # Post detail
    path('post/new/', PostCreateView.as_view(), name='post-create'),        # Create post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete post

    # =========================
    # COMMENT URLs
    # =========================
    path('posts/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Create comment
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),       # Update comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),       # Delete comment
]

