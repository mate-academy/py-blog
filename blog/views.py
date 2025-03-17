from django.shortcuts import render
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post

    def get_queryset(self):
        return Post.objects.select_related("owner").prefetch_related("commentary_set__user")