# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import User, Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    queryset = Post.objects.order_by("-created_time")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:index")


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "blog/blog_confirm_delete.view"
    success_url = reverse_lazy("blog:index")


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    fields = "__all__"
    context_object_name = "comment-create"
    template_name = "blog/commentary_form.html"
    success_url = reverse_lazy("blog:index")


class UserView(generic.ListView):
    model = User
