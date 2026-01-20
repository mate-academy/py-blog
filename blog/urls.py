from django.urls import path, include

from blog.views import PostListView, PostDetailView, commentary_create_view

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>", commentary_create_view, name="commentary-create")
]

app_name = "blog"
