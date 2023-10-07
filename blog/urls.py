from django.urls import path

from .views import (
    PostListView,
    PostDetailView, commentary_create_view,
)


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/comment/",
        commentary_create_view,
        name="commentary-create"
    ),
]

app_name = "blog"
