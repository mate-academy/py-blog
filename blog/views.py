from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    post_list = (
        Post.objects
        .select_related("owner")
        .prefetch_related("commentaries")
    )
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page", 1)
    posts = paginator.get_page(page_number)
    context = {
        "post_list": posts,
        "is_paginated": posts.has_other_pages(),
        "num_posts": post_list.count(),
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (
        Post.objects
        .select_related("owner")
        .prefetch_related("commentaries__user")
    )

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs) -> HttpResponse:
        form = CommentaryForm(request.POST)
        post = self.get_object()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)
