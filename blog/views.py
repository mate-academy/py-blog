from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import generic

from blog.models import Post, Commentary


def index(request):
    posts = Post.objects.all().order_by("created_time")
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    context = {
        "posts": page_obj,
    }
    return render(request,
                  "blog/index.html",
                  context=context, )


class PostDetailView(generic.DetailView):
    model = Post


@login_required
def add_comment(request, pk):
    if request.method == "POST":
        comment_content = request.POST.get("comment")
        if comment_content:
            post = Post.objects.get(id=pk)
            Commentary.objects.create(
                post=post,
                user=request.user,
                content=comment_content
            )
            messages.success(request, "Comment successfully added!")
        else:
            messages.warning(request, "A comment cannot be empty!")
    return redirect("blog:post-detail", pk=pk)
