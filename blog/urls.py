from tkinter.font import names

from django.urls import path

from .views import index, PostDetailView, comment_create, PostCreateView

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/comment/",
        comment_create,
        name="comment-create"
    ),
    path("post/create", PostCreateView.as_view(), name="post-create"),
]

app_name = "blog"
