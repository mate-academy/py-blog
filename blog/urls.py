from django.urls import path

from blog.views import PostsListView, PostDetailView

urlpatterns = [
    path("", PostsListView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

]

app_name = "blog"
