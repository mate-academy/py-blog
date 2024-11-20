from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-created_time"]
    paginate_by = 5


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:index")


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:my-post-list")


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:my-post-list")


class MyPostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "blog/my_post_list.html"
    ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    success_url = reverse_lazy("blog:index")
