from django.urls import path

from blog import views
from blog.views import PostDetailView, PostListView

urlpatterns = [
    path("", views.index, name="index"),
    path("page/<int:page>/", views.index, name="index-pagination"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
