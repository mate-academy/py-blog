from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    queryset = Post.objects.select_related('owner').prefetch_related('commentaries')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'