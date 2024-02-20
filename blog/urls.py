from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path(
        "posts/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post-detail"
    ),
]

app_name = "blog"
