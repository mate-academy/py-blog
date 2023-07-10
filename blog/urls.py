from django.urls import path

from blog.views import IndexView, PostDetailView, CommentaryAddView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "posts/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "posts/<int:pk>/commentary-add/",
        CommentaryAddView.as_view(),
        name="commentary-add",
    ),
]

app_name = "blog"
