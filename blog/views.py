from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic, View
from django.contrib.auth import get_user

from blog.forms import CommentForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(View):
    template_name = "blog/post_detail.html"
    model = Post

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        context = {
            "post": post,
            "comment_form": CommentForm()
        }
        return render(request, "blog/post_detail.html", context)

    def post(self, request, pk):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(id=pk)
        if comment_form.is_valid() and get_user(request).is_authenticated:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = get_user(request)
            comment.save()
            return HttpResponseRedirect(reverse("blog:post-detail", args=[pk]))

        error = "Please login for comments!"
        context = {
            "post": post,
            "comment_form": comment_form,
            "error": error,
        }
        return render(request, "blog/post_detail.html", context)
