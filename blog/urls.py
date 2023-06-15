from django.urls import path

# from blog.views import index
from blog.views import PostListView, UserListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("users/", UserListView.as_view(), name="user-list"),
    path(
        "posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"
    ),
]

app_name = "blog"
