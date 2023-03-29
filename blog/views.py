from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db.models import Count
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic

from blog.models import Post, Commentary


class PostListViews(generic.ListView):
    model = Post
    queryset = Post.objects.select_related(
        "owner"
    ).prefetch_related(
        "commentaries"
    ).order_by(
        "created_time"
    ).annotate(
        count_comments=Count("commentaries")
    )
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        content = request.POST.get("content")
        if not content:
            raise ValidationError("Comment cannot be empty!")
        comment, created = Commentary.objects.get_or_create(
            user=request.user,
            post=post,
            content=content
        )
        if created:
            return redirect("blog:post-detail", pk=post.pk)
        else:
            messages.warning(
                request,
                "Your comment has already been recorded!"
            )
