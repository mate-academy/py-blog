from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post, Commentary


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, generic.DeleteView):
    model = Post


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    context_object_name = "comment_create"
    fields = "__all__"
    success_url = reverse_lazy("taxi:post-detail")
