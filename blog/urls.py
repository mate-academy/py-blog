from blog.views import IndexView, PostDetailView, CommentaryCreateView
from django.urls import path

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/<int:pk>/create-commentary/",
        CommentaryCreateView.as_view(),
        name="commentary-create"),
]

app_name = "blog"
