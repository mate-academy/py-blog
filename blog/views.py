from django.shortcuts import render

from blog.models import Post
from django.views import generic


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    ordering = ['-created_time']
    

class IndexListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-created_time']
    paginate_by = 5