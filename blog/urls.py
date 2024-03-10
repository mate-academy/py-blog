from django.urls import path
from blog.views import (
    PostDetailView,
    UserListView,
    IndexListView,
)

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("user/", UserListView.as_view(), name="user-list"),
]

app_name = "blog"
