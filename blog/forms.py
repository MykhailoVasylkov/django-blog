from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    A form for creating a sing comment.
    """
    class Meta:
        model = Comment
        fields = ('body',)