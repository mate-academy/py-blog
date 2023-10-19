from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    ordering = "-created_time"
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentaries")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentaries", "commentaries__user")


@login_required
def add_commentary(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    commented_post = get_object_or_404(Post, pk=pk)
    content = request.POST.get("content")

    if request.method == "POST" and content:
        Commentary.objects.create(
            user=request.user,
            post=commented_post,
            content=content
        )
    return redirect(commented_post)
