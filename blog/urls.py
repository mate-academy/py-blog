from django.urls import path

from blog.views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:post_id>/commentary_form/",
        PostDetailView.as_view(),
        name="commentary-form"
    ),
]

app_name = "blog"
