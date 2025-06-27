from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    CustomUserListView,
                    CustomUserDetailView)


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("users/",
         CustomUserListView.as_view(),
         name="user-list"),
    path("users/<int:pk>/",
         CustomUserDetailView.as_view(),
         name="user-detail"),
    path(
        "blog/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
]


app_name = "blog"
