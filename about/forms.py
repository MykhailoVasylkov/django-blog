from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    A form for creating a collaboration request.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
