from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog/post_detail.html"
