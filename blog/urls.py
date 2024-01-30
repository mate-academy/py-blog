from django.urls import path

from blog.views import (
    index,
    PostDetailView,
    CommentCreate,
    RegistrateUserCreateView,
    log_out,
)

app_name = "blog"


urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/add_comment", CommentCreate.as_view(), name="create-comment"),
    path("register/", RegistrateUserCreateView.as_view(), name="register"),
    path("log_out/", log_out, name="log-out"),
]
