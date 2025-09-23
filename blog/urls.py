from django.urls import path

from blog.views import Index, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create-commentary/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
]

app_name = "blog"
