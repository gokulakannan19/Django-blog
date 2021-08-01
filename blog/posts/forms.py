from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth.models import User

from .models import *


class PostForm(forms.ModelForm):

    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 12}))

    class Meta:
        model = Post
        fields = ['title', 'body']


# class CreateUserForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
