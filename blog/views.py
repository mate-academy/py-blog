from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    ordering = ["-created_time"]
    paginate_by = 5
    queryset = (
        Post.objects.select_related("owner")
        .prefetch_related("commentaries")
        .annotate(num_comments=Count("commentaries"))
    )


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Commentary.objects.select_related("user").filter(post=post)
    user = request.user
    form = CommentaryForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "blog/post_detail.html", context=context)
