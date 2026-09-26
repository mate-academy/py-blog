from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexList.as_view(), name="index"),
    path(
        "posts/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post-detail"),
    path(
        "posts/<int:pk>/comments/",
        views.CommentaryCreateView.as_view(),
        name="comment-create",
    ),
]
