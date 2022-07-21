from dataclasses import field
import imghdr
from pyexpat import model
from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('name','email','body')