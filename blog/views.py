from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = (
        Post.objects
        .prefetch_related("commentaries")
        .select_related("owner")
        .order_by("-created_time")
    )
    template_name = "blog/index.html"
    paginate_by = 5
