from django.urls import path
from .views import (
    Index,
    post_detail_view,
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path(
        "posts/<int:pk>/",
        post_detail_view,
        name="post-detail",
    ),
]

app_name = "blog"
