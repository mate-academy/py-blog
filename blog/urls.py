from django.urls import path

from .views import PostDetailView, add_comment, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/add_comment/", add_comment, name="add-comment"),

]

app_name = "blog"
