from typing import Any, Dict
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import redirect, render

from .forms import CreateCommentForm
from .models import Post, Commentary


class PostListView(ListView):
    model = Post
    paginate_by = 5
    queryset = (
        Post.objects.select_related("owner")
        .prefetch_related("commentary_set")
        .all()
    )


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = CreateCommentForm(
            initial={"post": context["post"], "user": self.request.user},
        )
        return context


class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Commentary
    login_url = "/admin/"

    def post(self, request, *args, **kwargs):
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            form.save()
        post_id = form["post"].data
        return redirect("blog:post-detail", post_id)
