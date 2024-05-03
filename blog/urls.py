from django.urls import path
from blog.views import PostView, PostDetailView, CommentsCreateView


urlpatterns = [
    path("", PostView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create_comment/",
        CommentsCreateView.as_view(),
        name="comments-create",
    ),
]

app_name = "blog"
