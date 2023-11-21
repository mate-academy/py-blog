from django.urls import path

from blog import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path(
        "posts/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post-detail"
    ),
    path("posts/<int:pk>/add-comment/", views.add_comment, name="add-comment"),
]


app_name = "blog"
