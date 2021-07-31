from django.forms import ModelForm
from django import forms

from .models import *


class PostForm(forms.ModelForm):

    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 12}))

    class Meta:
        model = Post
        fields = ['title', 'body']
