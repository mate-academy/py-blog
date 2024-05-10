from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page", 1)
    posts = paginator.get_page(page_number)
    context = {
        "post_list": posts,
        "is_paginated": True if posts.has_other_pages() else False,
        "page_obj": posts,
        "paginator": paginator,
    }
    return render(request, "blog/index.html", context=context)


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/post_list.html"
    queryset = Post.objects.select_related("owner").order_by("-created_time")
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    queryset = Post.objects.select_related("owner")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs):
        post_object = self.get_object()
        new_comment = Commentary(
            content=request.POST.get("content"),
            user=self.request.user,
            post=post_object,
        )
        new_comment.save()
        return redirect("blog:post-detail", pk=post_object.pk)
