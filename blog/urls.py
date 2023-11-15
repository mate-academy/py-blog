from django.urls import path

from blog.views import PostListView, PostDetailView, create_comment

urlpatterns = [
    path("", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/comment/', create_comment, name='create_comment'),
]

app_name = "blog"
