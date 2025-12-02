from django.urls import path
from blog.views import index, PostDetailView, add_comment


app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/comment/", add_comment, name="post-comment"),
]
