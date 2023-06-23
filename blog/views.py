from django.urls import reverse_lazy

from blog.models import Post, Commentary
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]
    success_url = reverse_lazy("blog:post-detail")
    template_name = "blog/post_comment.html"
