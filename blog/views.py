from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import CommentaryForm
from .models import Commentary
from .models import Post


def index(request):
    post_list = Post.objects.order_by("-created_time")

    paginator = Paginator(post_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj.object_list,
        "page_obj": page_obj,
        "paginator": paginator,
    }

    return render(request, "blog/index.html", context)


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        comment_form = CommentaryForm()

        context = {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        }

        return render(request, "blog/post_detail.html", context=context)


class CreateCommentView(LoginRequiredMixin, View):
    login_url = "/accounts/"

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comment_form = CommentaryForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
        return redirect("blog:post-detail", pk=pk)


class UpdateCommentView(LoginRequiredMixin, View):
    login_url = "/accounts/"

    def post(self, request, comment_pk):
        comment = get_object_or_404(Commentary, pk=comment_pk)
        if comment.user == request.user:
            comment_form = CommentaryForm(request.POST, instance=comment)
            if comment_form.is_valid():
                comment_form.save()
        return redirect("blog:post-detail", pk=comment.post.pk)


class DeleteCommentView(LoginRequiredMixin, View):
    login_url = "/accounts/"

    def post(self, request, comment_pk):
        comment = get_object_or_404(Commentary, pk=comment_pk)
        if comment.user == request.user:
            comment.delete()
        return redirect("blog:post-detail", pk=comment.post.pk)
