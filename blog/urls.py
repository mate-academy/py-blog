from django.urls import path

from blog.views import PostDetailView, PostCreateView, PostListView, HomeView

urlpatterns = [
    path("",
         HomeView.as_view(),
         name="index"),
    path("post-list",
         PostListView.as_view(),
         name="post-list", ),
    path("posts/<int:pk>/",
         PostDetailView.as_view(),
         name="post-detail"),
    path("posts/<int:post_id>/add-comment/",
         PostCreateView.as_view(),
         name="add-comment"),
]

app_name = "blog"
