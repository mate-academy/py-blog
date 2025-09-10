
from django.urls import path

from blog.views import IndexView, PostDetailedView, CreateCommentView

app_name = "blog"


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailedView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comment-create/",
        CreateCommentView.as_view(),
        name="comment-create"
    ),
]
