from django.urls import path

from blog.views import (
    Index,
    PostDetailView,
    CommentaryCreateView,
)


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path(
        "posts/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "posts/<int:pk>/comments/add/",
        CommentaryCreateView.as_view(),
        name="commentary-add"
    )
]


app_name = "blog"
