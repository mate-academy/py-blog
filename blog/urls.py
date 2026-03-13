from django.urls import path
from .views import IndexView, PostDetailView, CommentaryCreateView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "comments/<int:pk>/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create",
    ),
]

app_name = "blog"
