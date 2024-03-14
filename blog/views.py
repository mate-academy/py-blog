from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class IndexListView(LoginRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ("content", )
    success_url = reverse_lazy("blog:post-detail")
