from django.urls import path, include
from django.conf.urls.static import static
from blog.views import UserListView, PostDetailView, PostListView
from blog_system import settings

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("users/", UserListView.as_view(), name="user-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("accounts/", include("django.contrib.auth.urls")),
]

app_name = "blog"
