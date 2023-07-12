from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

class BlogPostView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'