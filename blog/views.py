from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
