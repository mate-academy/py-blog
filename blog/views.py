from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post, Commentary


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    posts_list = Post.objects.all()
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, generic.DeleteView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("taxi:post-list")


class CommentaryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("taxi:post-list")


class CommentaryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("taxi:post-list")
