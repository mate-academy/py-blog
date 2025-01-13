from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all()
    all_comments = Commentary.objects.count()

    paginator = Paginator(post_list, 5)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)

    context = {
        "post_list": page_obj.object_list,
        "all_comments": all_comments,
        "page_obj": page_obj,
    }
    return render(request, "blog/index.html", context)


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.post = post
            comments.user = request.user
            comments.save()
            return redirect("blog:post-detail", pk=post.pk)
    else:
        form = CommentaryForm()

    comments = post.comments.all()
    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments, "form": form},
    )
