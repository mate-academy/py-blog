from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentaryForm
from django.shortcuts import get_object_or_404
from .models import Post
from .forms import PostForm


from django.core.paginator import Paginator


def index(request):
    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/index.html",
        {"page_obj": page_obj, "post_list": page_obj},
    )


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect("index")
    else:
        form = PostForm()
    return render(
        request,
        "blog/create_post.html",
        {"form": form}
    )


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.commentary_set.all().order_by("created_time")

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(
                request, "You must be logged in to add comments."
            )
            form = CommentaryForm()
        else:
            form = CommentaryForm(request.POST)
            if form.is_valid():
                commentary = form.save(commit=False)
                commentary.user = request.user
                commentary.post = post
                commentary.save()
                return redirect("post-detail", pk=pk)
    else:
        form = CommentaryForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comments": comments,
        "form": form,
    })
