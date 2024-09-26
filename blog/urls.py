from django.urls import path
from blog.views import Index, PostDetailView, CommentaryCreateView


app_name = "blog"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:post_pk>/commentary/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    )
]
