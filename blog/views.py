from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404

from blog.forms import CommentForm
from blog.models import Post


class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)
    context = {
        "post": post,
        "form": CommentForm(initial={"post": post, "user": request.user})
    }
    if request.user.is_authenticated:
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)
    else:
        form.fields["content"].widget.attrs["readonly"] = True

    return render(request, "blog/post_detail.html", context)
