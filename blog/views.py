from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post


class PostListViews(generic.ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 5


class PostDetailView(generic.View):
    template_name = "blog/post_detail.html"

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.select_related("user")
        new_comment = None
        comment_form = CommentForm()

        context = {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            "user": request.user
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.select_related("user")
        comment_form = CommentForm(request.POST)
        new_comment = None

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            content = comment_form.cleaned_data.get("content")
            new_comment.content = content
            new_comment.user = request.user
            new_comment.post = post
            new_comment.created_time = datetime.now()
            new_comment.save()
            return redirect("blog:post-detail", pk=pk)

        context = {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            "user": request.user
        }

        return render(request, self.template_name, context)
