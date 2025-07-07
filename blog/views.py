from django.db.models.aggregates import Count
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Post, Commentary, User


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.all().select_related(
        "owner").prefetch_related(
        "comments")
    paginate_by = 5


# class PostDetailView(generic.DetailView):
#     model = Post
#     template_name = "blog/posts.html"


def postdetailview(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        if request.user.is_authenticated:
            content = request.POST.get("content")
            Commentary.objects.create(
                post=post,
                user=request.user,
                content=content
            )
            return redirect("blog:post-detail", pk=pk)
        else:
            return redirect("blog:post-detail", pk=pk)
    return render(request, "blog/posts.html", {"post": post})
