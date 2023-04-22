from django.shortcuts import render, get_object_or_404
from django.views import generic

from .forms import CommentaryForm
from .models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner")
    template_name = "blog/index.html"
    paginate_by = 5


def post_detail_view(request, pk: int):
    post = get_object_or_404(Post, id=pk)

    if request.method == "POST":
        comment_form = CommentaryForm(request.POST)

        if comment_form.is_valid():
            comment_form = Commentary.objects.create(
                **comment_form.cleaned_data,
                post=post,
                user=request.user
            )
    else:
        comment_form = CommentaryForm()

    context = {
        "post": post,
        "comments": post.comments.select_related("post"),
        "comment_form": comment_form,
    }
    return render(request, "blog/post_detail.html", context=context)
