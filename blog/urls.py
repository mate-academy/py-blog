from django.urls import path

from .views import *

app_name = "blog"

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("index/", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/add_comment/",
        AddCommentView.as_view(),
        name="post-add-comment"
    ),
]
