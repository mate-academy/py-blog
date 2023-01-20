from django.urls import path, include

from blog.views import index, PostDetailView, AddCommentView

urlpatterns = [
    path("posts/", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("post/<int:pk>/add-comment", AddCommentView.as_view(), name="add_comment"),
]

app_name = "blog"
