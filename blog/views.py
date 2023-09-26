from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.models import Post, Commentary
from blog.forms import CommentForm


class Index(generic.ListView):
    model = Post
    queryset = Post.objects.order_by("created_time")
    template_name = "blog/index.html"
    paginate_by = 5


def post_detail_view(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == "GET":
        form = CommentForm(initial={"user": request.user})
        context = {"form": form, "post": post}
        return render(request, "blog/post_detail.html", context=context)

    if request.method == "POST":
        form = CommentForm(request.POST)
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
