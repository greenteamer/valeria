# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

class PostList(ListView):
    template_name = 'blog.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()

class PostDetail(DetailView):
    model = Post
    template_name = 'blog_detail.html'