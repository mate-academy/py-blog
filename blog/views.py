from django.shortcuts import render, redirect
from django.views.generic import ListView
from django import forms
from django.contrib import messages

from .models import Post, Commentary, User


class Index(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5
    queryset = Post.objects.select_related("owner").order_by("-created_time")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]
        labels = {
            "content": "Your Comment",
        }
        help_texts = {
            "content": None,
        }


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.commentaries.all().order_by("-created_time")

    form = CommentForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.warning(
                request,
                "You must be logged in to leave a commentary."
            )
            return redirect("blog:post-detail", pk=post.pk)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments, "form": form},
    )
