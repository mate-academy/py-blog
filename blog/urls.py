from django.urls import path

from .views import (
    Index,
    PostDetailView,
    CommentaryCreateView
)

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("post/<int:pk>/",
         PostDetailView.as_view(),
         name="post-detail"),
    path("post/<int:pk>/create_commentary/",
         CommentaryCreateView.as_view(),
         name="post-create-commentary")
]

app_name = "blog"
