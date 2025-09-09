from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)    # Extend UserCreationForm to include email

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    """
    Form for creating and updating comments.
    
    Uses Django's ModelForm to automatically generate form fields
    based on the Comment model. Includes validation to ensure content
    is not empty.
    """
    class Meta:
        model = Comment
        fields = ['content']  # Only allow editing the comment content
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment...'}),
        }
