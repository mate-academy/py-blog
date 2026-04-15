from typing import Any
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentaryForm
from .models import Post


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.select_related("owner")

    paginator = Paginator(posts, 5)
    page_number: str | None = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context: dict[str, Any] = {
        "page_obj": page_obj,
        "post_list": page_obj.object_list,
    }

    return render(request, "blog/index.html", context)


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.select_related("user")

    if request.method == "POST":
        form = CommentaryForm(request.POST)

        if request.user.is_authenticated:
            if form.is_valid():
                commentary = form.save(commit=False)
                commentary.user = request.user
                commentary.post = post
                commentary.save()
                return redirect("blog:post-detail", pk=pk)

        else:
            form.add_error(None, "You must be logged in to comment")
    else:
        form = CommentaryForm()

    context: dict[str, Any] = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog/post_detail.html", context)
