from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/index.html")


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post_detail"
    template_name = "blog/post_detail.html"
    queryset = Post.objects.prefetch_related("commentaries").all()


@login_required
def add_comment(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == 'POST':
        content = request.POST["content"]
        post_id = request.POST["post_id"]
        user_id = request.POST["user_id"]
        Commentary.objects.create(content=content, post_id=post_id, user_id=user_id)
    return redirect("blog:post-detail", pk=pk)
