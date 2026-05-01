from django.contrib.auth.decorators import login_required
from django.db.models import Count

from django.views import generic
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import DetailView

from blog.forms import CommentForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = (
        Post.objects.select_related("owner")
        .annotate(num_comments=Count("commentaries"))
        .order_by("-created_time")
    )
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post
    queryset = (Post.objects.select_related("owner")
                .prefetch_related("commentaries__user"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context


@login_required
def add_comment(request, pk):
    post_obj = get_object_or_404(
        Post.objects.select_related("owner")
        .prefetch_related("commentaries__user"),
        pk=pk
    )
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post_obj
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=pk)
        context = {
            "object": post_obj,
            "form": form,
            "comments": post_obj.commentaries.all()
        }
        return render(request, "blog/post_detail.html", context)
    return redirect("blog:post-detail", pk=pk)
