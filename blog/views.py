from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .models import User, Post, Commentary


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "blog/index.html"
    # context_object_name = "posts"
    queryset = Post.objects.order_by("-created_time")
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = "__all__"
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:index")


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = "blog/blog_confirm_delete.view"
    success_url = reverse_lazy("blog:index")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    context_object_name = "comment-create"
    template_name = "blog/commentary_form.html"
    success_url = reverse_lazy("blog:index")


class UserView(LoginRequiredMixin, generic.ListView):
    model = User
