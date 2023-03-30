from django.urls import path

from blog.views import IndexView, CommentsCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "blog/post/<int:pk>/",
        CommentsCreateView.as_view(),
        name="post-detail"
    ),
]

app_name = "blog"
