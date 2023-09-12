from django.db.models import Prefetch
from django.views import generic

from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    queryset = (
        Post.objects.order_by("-created_time").select_related("owner")
        .prefetch_related(
            Prefetch(
                "commentaries",
                queryset=Commentary.objects.select_related("user"),
                to_attr="total_commentaries"
            )
        )
    )
    template_name = "blog/index.html"
    paginate_by = 5
