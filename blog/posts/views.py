from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import Post
from .forms import PostForm, CreateUserForm


def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                print(f'Account successfully created for {username}')
                return redirect('login-page')
        context = {
            'form': form
        }
        return render(request, 'posts/register_page.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                print("Username or password is incorrect")

        context = {}
        return render(request, 'posts/login_page.html', context)


def logout_user(request):
    logout(request)
    return redirect('login-page')


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
