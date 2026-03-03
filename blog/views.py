from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.shortcuts import redirect

from .models import Post, Commentary
from .forms import CommentForm


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Commentary

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get("content")
            Commentary.objects.create(
                user=request.user,
                post=Post.objects.get(pk=kwargs.get("pk")),
                content=content
            )
        return redirect("blog:post-detail", *args, **kwargs)
