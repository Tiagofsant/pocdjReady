# blog/views.py
from django.shortcuts import render
from .models import Post

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/lista_posts.html', {'posts': posts})
