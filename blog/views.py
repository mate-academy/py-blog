from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = Post.objects.order_by("-created_time")


class HomeView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = ""
    paginate_by = 5
    queryset = Post.objects.order_by("-created_time")


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    queryset = Post.objects.select_related("owner").order_by("-created_time")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post-list")
    template_name = "blog/add_comment.html"
