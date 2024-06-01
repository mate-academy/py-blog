from blog.views import index_view, PostDetailView, comment_view
from django.urls import path


app_name = "blog"

urlpatterns = [
    path("", index_view, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("comment/<int:post_id>/", comment_view, name="comment"),
]
