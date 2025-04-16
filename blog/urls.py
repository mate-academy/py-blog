from django.urls import path

from .views import IndexView, PostDetailView, PostCreateView

urlpatterns = [
    path(
        "posts/",
        IndexView.as_view(),
        name="index"
    ),
    path(
        "posts/<int:pk>",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "posts/<int:pk>/create/",
        PostCreateView.as_view(),
        name="post-create"
    ),
]


app_name = "blog"
