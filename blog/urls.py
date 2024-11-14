from django.urls import path
from django.contrib.auth import views as auth_views

from blog.views import PostListView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "posts/<int:pk>/new-commentary/",
        CommentaryCreateView.as_view(),
        name="commentary-create",
    ),
]


app_name = "blog"
