from django.urls import path
from .views import PostListView, PostDetailView, CommentFormView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("create/<int:pk>/",
         CommentFormView.as_view(),
         name="comment-create"
         ),
]
