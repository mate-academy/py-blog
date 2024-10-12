from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries"
    )
    paginate_by = 5


def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    user = request.user
    post = Post.objects.prefetch_related("commentaries__user").get(id=pk)
    form = CommentaryForm(request.POST or None)
    if form.is_valid():
        form.cleaned_data["user"], form.cleaned_data["post"] = user, post
        Commentary.objects.create(**form.cleaned_data)

        return HttpResponseRedirect(
            reverse("blog:post-detail", kwargs={"pk": pk})
        )

    return render(
        request, "blog/post_detail.html", context={"post": post, "form": form}
    )
