from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    queryset = (Post.objects.all().order_by("-created_time")
                .select_related("owner"))
    paginate_by = 5
    model = Post


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("comm_post__user")
