from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from blog.models import Post, Commentary


class PostListView(ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(DetailView):
    model = Post


@login_required
def create_commentary(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == "POST":
        content = request.POST["content"]
        post_id = request.POST["post_id"]
        user_id = request.POST["user_id"]
        created_time = datetime.now()
        Commentary.objects.create(
            content=content, post_id=post_id,
            user_id=user_id,
            created_time=created_time
        )
    return redirect("blog:post-detail", pk=pk)
