from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related("commentary_set")
    ordering = ("-created_time",)
    paginate_by = 5


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related("commentary_set")
    form_class = CommentaryForm


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = "__all__"
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        redirect_url = reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )
        return f"{redirect_url}#last-comment"
