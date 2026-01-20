from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.annotate(
        comment_count=Count("comments")
    ).order_by("-created_time").prefetch_related("comments")

    paginator = Paginator(posts, 5)  # 5 постів на сторінку
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj,
        "paginator": paginator,
        "is_paginated": page_obj.has_other_pages(),
        "page_obj": page_obj
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.annotate(
        comment_count=Count("comments")
    ).prefetch_related("comments")


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["content"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = get_object_or_404(Post, pk=self.kwargs["post_pk"])
        return context

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["post_pk"]}
        )
