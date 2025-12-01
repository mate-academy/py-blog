from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by("-created_time")


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentaryForm()

        context = {
            "post": post,
            "form": form,
        }

        return render(request, "blog/post_detail.html", context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentaryForm(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = post
            commentary.save()
            return redirect("blog:post-detail", pk=pk)

        context = {
            "post": post,
            "form": form,
        }

        return render(request, "blog/post_detail.html", context)
