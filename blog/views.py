from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.models import Post, Commentary
from django.views import generic
from django.urls import reverse_lazy


class PostView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:post-detail", kwargs={"pk": 1})
    template_name = "blog/commentary_create.html"
