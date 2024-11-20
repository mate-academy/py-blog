from django.contrib.auth import get_user_model
from django.db.models import Count
from django.db.models.query import QuerySet


def get_authors_with_post_counts() -> QuerySet:
    authors_with_post_counts = (
        get_user_model()
        .objects.annotate(post_count=Count("posts"))
        .filter(post_count__gt=0)
    )
    return authors_with_post_counts
