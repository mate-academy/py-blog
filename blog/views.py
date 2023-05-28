from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, redirect

from blog.models import Post, Commentary, User
from blog.forms import CommentaryForm


def index(request):
    post_list = Post.objects.order_by("-created_time")

    # info about blog
    num_users = User.objects.count()
    num_posts = Post.objects.count()

    if "page" in request.GET:
        page = request.GET["page"]
    else:
        page = 1
    paginator = Paginator(post_list, 5)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    context = {
        "post_list": post_list,
        "num_users": num_users,
        "num_posts": num_posts,
        "page": page
    }

    return render(request, "blog/index.html", context=context)


def post_detail_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)

        comment_to_post = Commentary.objects.filter(post=post)
        comment_count = Commentary.objects.filter(post=post).count()
        if request.method == "POST":
            if request.user.is_authenticated:
                form = CommentaryForm(request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.user = request.user
                    comment.post = post
                    comment.save()
                    return redirect("blog:post-detail", pk=pk)

            else:
                form = CommentaryForm()
                form.add_error(
                    None,
                    "Only authorized users can post comments."
                )
        else:
            form = CommentaryForm()
    except Post.DoesNotExist:
        raise Http404("Posts does not exist")
    context = {
        "post": post,
        "comment_count": comment_count,
        "comment_to_post": comment_to_post,
        "form": form,
    }

    return render(request, "blog/post_detail.html", context=context)
