from django.urls import path

from .views import index, PostDetailView, comment_create, PostCreateView

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(), name="post-create"),
    path(
        "posts/<int:pk>/comment/",
        comment_create,
        name="comment-create"
    ),

]

app_name = "blog"
