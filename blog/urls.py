from django.urls import path

from blog.views import IndexView, PostDetailView, UserListView, CommentaryCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/",
         PostDetailView.as_view(),
         name="post-detail"),
    path("users/",
         UserListView.as_view(),
         name="user-list")
]

app_name = "blog"
