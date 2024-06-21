from django.urls import path

from blog.views import index, PostDetailView, CommentCreateView


urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/add-comment/",
        CommentCreateView.as_view(),
        name="post-detail-add-comment"
    ),
]

app_name = "blog"
