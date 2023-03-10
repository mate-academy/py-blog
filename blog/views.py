from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = "post_view"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:index")


class CommentaryCreateView(
    LoginRequiredMixin,
    generic.CreateView
):
    model = Commentary
    template_name = "blog/commentary_form.html"
    fields = ["content"]
    success_url = reverse_lazy("blog:post-detail")
