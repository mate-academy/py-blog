from django.urls import path

from blog.views import PostListView, post_detail_and_add_commentary

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path(
        "posts/<int:pk>/",
        post_detail_and_add_commentary,
        name="post-detail"
    ),
]

app_name = "blog"
