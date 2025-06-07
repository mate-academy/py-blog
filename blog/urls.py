from django.urls import path

from blog.views import index, PostDetailView, CommentaryCreateView


urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:post_pk>/comment/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
]

app_name = "blog"
