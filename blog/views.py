import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import generic


from blog.models import Post, Commentary


class IndexListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


@login_required
def create_commentary(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == "POST":
        content = request.POST["content"]
        post_id = request.POST["post_id"]
        user_id = request.POST["user_id"]
        created_time = datetime.datetime.now()
        Commentary.objects.create(
            content=content,
            post_id=post_id,
            user_id=user_id,
            created_time=created_time
        )
    return redirect("blog:post-detail", pk=pk)
