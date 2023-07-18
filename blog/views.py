from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post


class MainView(generic.ListView):
    model = Post
    queryset = Post.objects.prefetch_related(
        "comments"
    ).order_by("-created_time")
    template_name = "blog/index.html"
    paginate_by = 5


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)
    else:
        form = CommentaryForm()
    return render(request,
                  "blog/post_detail.html",
                  context={
                      "post": post,
                      "form": form}
                  )
