from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views import View, generic
from django.db.models import Count
from django import forms
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Commentary
from .forms import CommentForm


class Posts(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    queryset = (
        Post.objects.order_by("-created_time")
        .prefetch_related("commentaries")
        .annotate(commetaries_count=Count("commentaries"))
    )
    context_object_name = "post_list"


class PostDetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        comments = post.commentaries.all()

        form = CommentForm()

        context = {
            "post": post,
            "comments": comments,
            "form": form,
        }
        return render(request, "blog/post_detail.html", context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = post
            commentary.user = (
                request.user
            )
            commentary.save()

            return redirect(
                reverse("blog:post-detail", kwargs={"pk": post.pk})
            )

        comments = post.commentaries.all()
        context = {
            "post": post,
            "comments": comments,
            "form": form,
        }
        return render(request, "blog/post_detail.html", context)
