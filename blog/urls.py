from django.urls import path

from blog.views import index, PostDetailViewWithComment

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailViewWithComment.as_view(), name="post-detail"),
]

app_name = "blog"
