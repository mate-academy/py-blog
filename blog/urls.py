from django.urls import path

from blog.views import IndexView, PostDetailWithCommentView


app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "posts/<int:pk>/",
        PostDetailWithCommentView.as_view(),
        name="post-detail"
    ),
]
