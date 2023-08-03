from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from datetime import datetime

from blog.models import Post, Commentary
from blog.forms import CommentaryForm


class PostListView(generic.ListView):
    model = Post
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("post_commentaries")


def commentary_create_view(request, pk: int):
    if request.method == "GET":
        context = {
            "form": CommentaryForm(),
            "post": Post.objects.get(id=pk)
        }

        return render(request, "blog/post_detail.html", context=context)

    if request.method == "POST":
        if request.user.is_authenticated:
            initial_data = {
                "post_id": pk,
                "user_id": Post.objects.get(id=pk).owner_id,
            }
            form_data = request.POST.copy()
            form_data.update(initial_data)
            form = CommentaryForm(form_data)

            if form.is_valid():
                Commentary.objects.create(**form.cleaned_data)
                return HttpResponseRedirect(
                    reverse("blog:post-detail", args=[pk])
                )
        context = {
            "form": CommentaryForm(),
            "post": Post.objects.get(id=pk)
        }
        return render(request, "blog/post_detail.html", context=context)
