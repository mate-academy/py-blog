from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic

from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    queryset = (
        Post.objects.select_related("owner")
        .annotate(comments_count=Count("comments"))
        .order_by("-created_time")
    )
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        content = request.POST.get("content")
        if content:
            Commentary.objects.create(
                user=request.user, post=post, content=content
            )
            return redirect("blog:post-detail", pk=post.pk)
        raise ValidationError("Empty comment is restricted!")
