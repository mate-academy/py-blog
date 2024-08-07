from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner").prefetch_related("comments")


class PostDetailView(generic.DetailView):
    model = Post
