from django.urls import path
from blog.views import (
    Index,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    UserListView,
    UserDetailView,
    CommentaryCreateView,
    UserCreateView,
)

urlpatterns = [
    path("user/", UserListView.as_view(), name="user-list"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("user/create/", UserCreateView.as_view(), name="user-create"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/",
         PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/",
         PostDeleteView.as_view(), name="post-delete"),
    path(
        "post<int:pk>/commentary/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create",
    ),
    path("blog/", Index.as_view(), name="index"),
]

app_name = "blog"
