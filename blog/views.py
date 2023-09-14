from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from blog.form import CommentForm
from blog.models import Commentary

from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    context_object_name = "post_list"


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        "post": post,
        "form": CommentForm()
    }
    if request.method == "GET":
        return render(request, "blog/post_detail.html", context=context)

    elif request.method == "POST":
        content = request.POST.get("content")
        Commentary.objects.create(user=request.user, post=post, content=content)
        return redirect(reverse_lazy("blog:post-detail", args=[post.pk]))
