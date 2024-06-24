from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'thumbnail', 'category', 'featured']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Join the discussion and leave a comment!'}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Leave a reply!'}),
        }
