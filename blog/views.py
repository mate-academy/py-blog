from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .forms import CommentForm
from .models import Post, Commentary


def index(request):
    context = {"posts": Post.objects.all()}
    return render(request, "index_list.html", context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"


class CreateCommentView(generic.CreateView):
    template_name = "post_detail.html"

    def get(self, request, pk) -> HttpResponse:
        post = get_object_or_404(Post, pk=pk)
        return render(
            request, "post_detail.html", {"post": post, "form": CommentForm()}
        )

    def post(self, request, pk) -> HttpResponse:
        post = get_object_or_404(Post, pk=pk)
        date = request.POST.get("created_time")
        content = request.POST.get("content")
        Commentary.objects.create(
            user=request.user, post=post, content=content, created_time=date
        )
        return redirect("blog:comments-creates", pk)
