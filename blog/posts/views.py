from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('created_at',)[::-1]
    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post
    }
    return render(request, 'posts/post.html', context)
