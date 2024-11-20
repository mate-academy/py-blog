from django.urls import path

from blog import views
from .views import PostDetailView, CommentaryCreateView

app_name = "blog"  # Specify the app namespace

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "post/<int:pk>/",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "post/<int:pk>/commentary/create/",
        CommentaryCreateView.as_view(),
        name="commentary-create"
    ),
]
