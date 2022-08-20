from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostView(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'news/postlist.html'
    context_object_name = 'postlist'


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


