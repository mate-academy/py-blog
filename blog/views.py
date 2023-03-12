from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Post, User, Commentary


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PostListView(generic.ListView):
    model = Post
    template_name = "post_list.html"
    ordering = ["-created_time"]
    context_object_name = "index"
    paginate_by = 5
    # add buttons to prev, next, num_lists


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    template_name = "includes/commentary_form.html"
    success_url = reverse_lazy("blog:post-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs.get("pk"))
        return super().form_valid(form)


    # change url, somehow that render current page without redirect on commentary page
