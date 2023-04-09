from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Count
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from blog.models import Commentary, Post
from blog.forms import CommentaryForm


def index(request: HttpRequest) -> HttpResponse:
    num_users = get_user_model().objects.count()
    num_posts = Post.objects.count()
    num_comments = Commentary.objects.count()
    posts_list = (
        Post.objects.select_related("owner")
        .annotate(Count("comments")).order_by("-created_time")
    )
    paginator = Paginator(posts_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "num_users": num_users,
        "num_posts": num_posts,
        "num_comments": num_comments,
        "post_list": page_obj,
    }

    return render(request, "blog/index.html", context)


def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    post = (
        Post.objects.filter(id=pk).select_related("owner")
        .annotate(Count("comments")).first()
    )
    comments = (
        Commentary.objects.filter(post__id=pk)
        .select_related("user").order_by("created_time")
    )

    form = CommentaryForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("blog:post-detail", pk=post.id)

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog/post_detail.html", context)


@login_required
def user_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    user = (
        get_user_model()
        .objects.filter(id=pk)
        .annotate(Count("posts"), Count("comments")).first()
    )

    context = {
        "author": user,
    }

    return render(request, "blog/user_detail.html", context)
