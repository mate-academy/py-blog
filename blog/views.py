from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views import generic

from blog.models import Post, Commentary


class IndexListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post


def comment_create(request: HttpRequest) -> HttpResponse:
    pk = request.POST["num-of-post"]
    comment = request.POST["comment"]
    user_id = request.POST["user-id"]

    Commentary.objects.create(content=comment, user_id=user_id, post_id=pk)
    return redirect(f"/posts/{pk}/")
