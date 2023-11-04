from django.urls import path

from blog.views import IndexView, PostDetailView, add_new_comment

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/add-comment/", add_new_comment, name="add-comment"),
]

app_name = "blog"
