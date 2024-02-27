from django.shortcuts import redirect
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Post, Commentary
from .form import CreateCommentForm


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/index.html"
    queryset = (
        Post.objects.select_related("owner")
        .prefetch_related("comments")
        .order_by("-created_time")
    )


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related("comments")

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["create_comment"] = CreateCommentForm()

        return context

    @method_decorator(login_required)
    def post(self, *args, **kwargs):
        post = self.get_object()

        create_comment = CreateCommentForm(data=self.request.POST)

        if create_comment.is_valid():
            comment = create_comment.save(commit=False)
            comment.user = self.request.user
            comment.post = post
            comment.save()

        return redirect("blog:post-detail", pk=post.id)
