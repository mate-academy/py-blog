from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from blog.forms import CommentaryForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.select_related(
        "owner"
    ).prefetch_related(
        "comments"
    )
    paginator = Paginator(post_list, 5)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    context = {
        "post_list": page_obj,
        "page_obj": page_obj,
    }
    return render(request, "blog/index.html", context)


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = (
        Post.objects.select_related(
            "owner"
        ).prefetch_related("comments").get(pk=pk)
    )
    new_comment = None
    if request.user.is_authenticated and request.method == "POST":
        comment_form = CommentaryForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = CommentaryForm()
    context = {
        "post": post,
        "comment_form": comment_form,
        "new_comment": new_comment,
    }
    return render(request, "blog/post_detail.html", context)
