from django.urls import path

from .views import PostDetailView, PostListView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("blog/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(r"blog/create/<pk>",
         CommentaryCreateView.as_view(),
         name="commentary-create",),
]

app_name = "blog"
