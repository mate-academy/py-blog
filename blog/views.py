from django.shortcuts import render
from django.views import generic

from .forms import CommentaryForm
from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    template_name = "blog/index.html"
    paginate_by = 5


def post_detail_view(request, pk: int):
    post = Post.objects.select_related("owner").filter(id=pk).first()

    if not post:
        return render(request, "blog/post_not_found.html")

    if request.method == "POST":
        comment_form = CommentaryForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
    else:
        comment_form = CommentaryForm()

    context = {
        "post": post,
        "comments": post.comments.select_related("post"),
        "comment_form": comment_form,
    }
    return render(request, "blog/post_detail.html", context=context)
