from django.urls import path
from blog.views import IndexView, PostDetailView, AddCommentView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/add_comment/",
        AddCommentView.as_view(),
        name="post-add-comment"
    ),
]

app_name = "blog"
