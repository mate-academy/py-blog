from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class Index(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = Post.objects.order_by("-created_time")


def post_detail_view(request: HttpRequest, pk) -> HttpResponse:
    post = Post.objects.get(id=pk)

    if request.method == "GET":
        form = CommentaryForm(initial={"user": request.user})
        context = {"form": form, "post": post}
        return render(request, "blog/post_detail.html", context=context)

    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if request.user.is_anonymous:
            form.add_error("content", "Please log in to add a comment")
        elif form.is_valid():
            Commentary.objects.create(
                user=request.user, post=post, **form.cleaned_data
            )
            return HttpResponseRedirect(
                reverse("blog:post-detail", kwargs={"pk": pk})
            )

        context = {"form": form, "post": post}

        return render(request, "blog/post_detail.html", context=context)
