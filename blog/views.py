from django.urls import reverse_lazy

from .models import User, Post, Commentary
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
    template_name = "blog/comment_create.html"
