from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.form import CommentForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 5


def post_detail_view(request, pk):
    if request.method == "GET":
        post = Post.objects.get(id=pk)
        context = {"post": post}
        return render(request, "blog/post_detail.html", context=context)
    if request.method == "POST":
        creation_form = CommentForm(request.POST or None)
        if creation_form.is_valid():
            content = request.POST.get("content")
            comment = Commentary.objects.create(
                post=Post.objects.get(id=pk),
                user=request.user,
                content=content
            )
            comment.save()
            return HttpResponseRedirect(
                reverse(
                    "blog:post-detail", args=[str(pk)]
                )
            )

        else:
            post = Post.objects.get(id=pk)
            context = {"error": "Comment should not be empty!", "post": post}
            return render(request, "blog/post_detail.html", context=context)
