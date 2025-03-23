from django.urls import path

from blog.views import (
    CommentaryCreateView,
    HomePageView,
    PostsListView,
    PostsDetailView,
)

app_name = "blog"
urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("posts/", PostsListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostsDetailView.as_view(), name="post-detail"),
    path(
        "commentary/<int:post_pk>/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create",
    ),
]
