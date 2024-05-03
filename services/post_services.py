from django.db.models import QuerySet

from blog.models import Post


def get_posts(comments: bool = False) -> QuerySet:
    queryset = (
        Post.objects.select_related(
            "owner").prefetch_related("commentaries")
    )
    if comments:
        queryset = queryset.prefetch_related("commentaries__user")
    return queryset
