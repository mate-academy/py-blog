from django.urls import path

from blog.views import IndexListView, PostDetailView, CreateCommentView

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("comment/<int:pk>/", CreateCommentView.as_view(), name="comment-create"),
]

app_name = "blog"
