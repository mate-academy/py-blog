from django.urls import path

import blog.views as views


urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path(
        "posts/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post-detail"
    ),
    path("add-comment/", views.CommentaryCreateView.as_view(), name="add-comment"),
]

app_name = "taxi"
