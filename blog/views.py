from django.shortcuts import render
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.all().order_by("created_time")
    paginate_by = 5
