from django.contrib import admin
from django.urls import path
from blog.views import index, PostDetailView, SendCommentView

urlpatterns = [
    path("", index.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/", SendCommentView.as_view(), name="send-comment")
]

app_name = "blog"
