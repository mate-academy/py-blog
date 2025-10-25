from django.urls import path, include

from blog import views
from blog.views import PostDetailView

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "posts/detail/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
]

app_name = "blog"
