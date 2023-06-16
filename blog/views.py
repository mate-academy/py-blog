from typing import Callable

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post-list.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    template_name = "blog/add_commentary.html"
    fields = ["content"]
    success_url = "/"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.post = post
        form.instance.user = self.request.user
        return super().form_valid(form)
