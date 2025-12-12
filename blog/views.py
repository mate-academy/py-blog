from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.urls import reverse

from .models import Post
from .forms import CommentaryForm


def index(request):
    queryset = Post.objects.all().order_by("-created_time")
    paginator = Paginator(queryset, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "post_list": page_obj,
    }

    return render(request, "blog/index.html", context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return render(request, "blog/post_detail.html", {
                "post": post,
                "comments": comments,
                "form": CommentaryForm(request.POST)
            })

        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=pk)
    else:
        form = CommentaryForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form
    })
