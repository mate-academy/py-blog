from django.urls import path

from .views import Index, PostDetailView, CommentCreateView


app_name = "blog"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("commentary/<int:post_pk>/create/", CommentCreateView.as_view(), name="post-create")
]