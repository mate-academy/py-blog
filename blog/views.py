from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5


def post_detail_view(request, pk):
    if request.method == "GET":
        post = Post.objects.get(id=pk)
        context = {"post": post, "form": CommentaryForm()}
        return render(request, "blog/post_detail.html", context=context)

    if request.method == "POST":
        form = CommentaryForm(request.POST or None)
        if form.is_valid():
            content = request.POST.get("content")
            Commentary.objects.create(
                post=Post.objects.get(id=pk),
                user=request.user,
                content=content
            )
            return HttpResponseRedirect(reverse("blog:index"))

        else:
            post = Post.objects.get(id=pk)
            context = {
                "error": "Comment should not be empty!",
                "post": post,
                "form": form,
            }
            return render(request, "blog/post_detail.html", context=context)
