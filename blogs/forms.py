from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your post content here...'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Your Comment'
        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }