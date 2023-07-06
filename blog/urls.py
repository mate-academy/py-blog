from django.urls import path
from .views import PostListView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/create-commentary",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
]

app_name = "blog"
