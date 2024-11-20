from django.urls import path

from .views import IndexListView, PostDetailView, CommentaryCreateView

app_name = "blog"

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "post/<int:pk>/new_commentary/",
        CommentaryCreateView.as_view(),
        name="commentary-detail",
    ),
]
