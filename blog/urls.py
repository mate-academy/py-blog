from django.urls import include, path
from .views import (
    IndexView,
    PostDetailView,
    CommentaryCreateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    path(
        "post/<int:pk>/detail",
        PostDetailView.as_view(),
        name="post-detail"
    ),

    path(
        "posts/<int:pk>/add_comment/",
        CommentaryCreateView.as_view(),
        name="add-comment"
    ),

]


app_name = "blog"
