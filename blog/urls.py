
from django.urls import path

from blog.views import IndexView, PostDetailedView, CreateCommentView

app_name = "blog"


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailedView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/commnt-create",
        CreateCommentView.as_view(),
        name="comment-create"
    ),
]
