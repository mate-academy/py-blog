from django.urls import path
from . import views

from blog.views import IndexListView, PostDetailView

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "<int:pk>/create-comment",
        views.CreateCommentView.as_view(),
        name="create-comment"
    ),
]

app_name = "blog"
