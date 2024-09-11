from django.urls import path

from .views import Index, PostDetailView, add_commentary

app_name = "blog"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:post_id>/add_commentary/",
        add_commentary,
        name="add-commentary"
    ),
]
