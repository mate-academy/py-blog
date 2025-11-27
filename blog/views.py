from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import redirect
from django.views import generic

from .models import Post, Commentary


# Create your views here
class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.annotate(num_comments=Count("commentaries"))


class PostDetailView(generic.DetailView):
    model = Post
    ordering = ["-created_time"]

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        content = request.POST.get("content")
        if content and request.user.is_authenticated:
            Commentary.objects.create(
                user=request.user,
                post=post,
                content=content,
            )
        return redirect("blog:post-detail", pk=post.pk)
