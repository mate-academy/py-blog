from django.urls import path, include

from blog.views import PostListView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "<int:pk>/commentary-create/",
        CommentaryCreateView.as_view(),
        name="commentary-create",
    ),
]

app_name = "blog"
