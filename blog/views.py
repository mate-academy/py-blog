from datetime import datetime

from django.db.models import Count
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic

from blog.forms import CommentForm
from blog.models import Post


class MainView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "index.html"


def post_detail(request, pk):
    template_name = "blog/post_detail.html"
    post = get_object_or_404(Post, pk=pk)
    comments = post.commentaries.select_related("user")
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            content, post_id, user_id = comment_form.cleaned_data.values()
            print(content, user_id, post_id)
            new_comment.content = content
            new_comment.user_id = user_id
            new_comment.post_id = post_id
            new_comment.created_time = datetime.now()
            new_comment.save()
            return redirect("blog:post-detail", pk=post_id)

    comment_form = CommentForm()

    context = {
        "post": post,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
        "user": request.user
    }

    return render(request, template_name, context)
