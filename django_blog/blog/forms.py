from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from taggit.forms import TagWidget



# =========================
# USER AUTH FORMS
# =========================

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# =========================
# BLOG POST FORM
# =========================

class PostForm(forms.ModelForm):
    # Tags input as comma-separated string
    tags = forms.CharField(
        required=False,
        label='Tags',
        help_text='Comma-separated (e.g. django, python, tips)',
        widget=forms.TextInput(attrs={
            'placeholder': 'tag1, tag2, tag3',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Post title',
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your post...',
                'class': 'form-control',
                'rows': 8
            }),
        }



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # ✅ include tags
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Post title',
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your post...',
                'class': 'form-control',
                'rows': 8
            }),
            'tags': TagWidget(attrs={
                'class': 'form-control',
                'placeholder': 'Add tags separated by commas'
            }),  # ✅ Add this for tagging
        }




# =========================
# COMMENT FORM
# =========================

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your comment...',
                'class': 'form-control',
                'rows': 4
            }),
        }




