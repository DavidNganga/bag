from .models import Blog,Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = {}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=["content","name"]
