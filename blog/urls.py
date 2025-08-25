from django.contrib import admin
from django.urls import path
from blog.views import Index, PostDetailView, SendCommentView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/", SendCommentView.as_view(), name="send-comment")
]

app_name = "blog"
