from django.urls import path

from blog.views import IndexView, PostDetailView, CommentaryCreateView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/comment/",
        CommentaryCreateView.as_view(),
        name="post-create-comment"
    ),
]

app_name = "blog"
