from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries"
    )


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    pass


def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    form = CommentaryForm(request.POST or None)
    post = Post.objects.get(pk=pk)
    commentaries = post.commentaries.select_related("user")

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        form.save()
        return HttpResponseRedirect(reverse(
            "blog:post-detail",
            kwargs={"pk": pk}
        ))

    return render(
        request,
        "blog/post_detail.html",
        context={
            "post": post,
            "form": form,
            "commentaries": commentaries
        }
    )
