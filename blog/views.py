from django.shortcuts import render
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
