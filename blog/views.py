import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post


@login_required
def create_comment(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == "POST":
        content = request.POST["content"]
        post_id = request.POST["post_id"]
        user_id = request.POST["user_id"]
        created_time = datetime.datetime.now()
        Commentary.objects.create(
            content=content,
            post_id=post_id,
            user_id=user_id,
            created_time=created_time,
        )
    return redirect("blog:post-detail", pk=pk)
