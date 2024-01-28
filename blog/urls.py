from django.urls import path

from .views import index, PostDetailView, CommentaryCreateView

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/new_commentary",
        CommentaryCreateView.as_view(),
        name="commentary-detail",
    ),
]
