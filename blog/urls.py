from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "posts/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post-detail"
    ),
]
