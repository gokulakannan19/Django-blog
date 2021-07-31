from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


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


def create_post(request):

    form = PostForm()

    if request.method == 'POST':
        print("Printing post", request.POST)
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'posts/create_post.html', context)


def update_post(request, pk):

    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'posts/update_post.html', context)


def delete_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('/')

    return render(request, 'posts/delete_post.html')
