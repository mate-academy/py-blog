from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.core.exceptions import ValidationError

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post


def add_comment(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == "POST":
        user = request.user
        if not user.is_authenticated:
            raise ValidationError("User has to be authenticated!")
        post_id = request.POST.get("post_id")
        content = request.POST.get("content")
        post = Post.objects.get(pk=post_id)
        Commentary.objects.create(
            user=user,
            post=post,
            content=content,
        )
        return redirect("blog:post-detail", pk=post_id)
