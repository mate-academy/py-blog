from django.urls import path
from blog.views import PostView, PostDetailView, CommentaryCreateView

urlpatterns = [
    path("posts/", PostView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("commentary/create/", CommentaryCreateView.as_view(), name="commentary-create")
]

app_name = "blog"
