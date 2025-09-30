from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.aggregates import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, View

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(ListView):
    model = Post.objects.order_by("-created_time")
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.annotate(num_comments=Count("comments"))


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.prefetch_related("comments")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


# class CommentaryCreateView(CreateView):
#     model = Commentary
#     fields = ("content",)
#     template_name = "blog/post_detail.html"
#     success_url = reverse_lazy("blog:post-detail")
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         post_pk = self.kwargs.get("pk")
#         form.instance.post = Post.objects.get(pk=post_pk)
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy("blog:post-detail",
#                             kwargs={"pk": self.kwargs["pk"]})


class CommentaryCreateView(LoginRequiredMixin, CreateView):
    model = Commentary
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        post_pk = self.kwargs.get("pk")
        form.instance.post = get_object_or_404(Post, pk=post_pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("blog:post-detail",
                       kwargs={"pk": self.kwargs.get("pk")})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_pk = self.kwargs.get("pk")
        post = get_object_or_404(Post, pk=post_pk)
        context["post"] = post
        context["comments"] = post.comments
        return context
