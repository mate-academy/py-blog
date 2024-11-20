from django.urls import path
from .views import index, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
]

app_name = "blog"
