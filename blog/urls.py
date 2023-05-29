from django.urls import path

from blog.views import index, PostDetailView, CommentCreateView

urlpatterns = [
    path("", index, name="index"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "<int:pk>/comment/",
        CommentCreateView.as_view(),
        name="comment-create"
    ),

]

app_name = "blog"
