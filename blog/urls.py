from django.urls import path

from blog.views import Index, PostDetailView, CreateCommentaryView

urlpatterns = [
    path(
        "",
        Index.as_view(),
        name="index"
    ),
    path(
        "post/<int:pk>",
        PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        "post/<int:pk>/comment/",
        CreateCommentaryView.as_view(),
        name="create-comment"
    ),
]

app_name = "blog"
