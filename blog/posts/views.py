from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'posts/index.html', context)
