from django.urls import path

from blog.views import PostListView, PostDetailView, CommentaryCreateView


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path(
        "post/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path("post/",
         CommentaryCreateView.as_view(),
         name="commentary-create"),
]

app_name = "blog"
