from django.urls import path, include

from blog.views import Index, PostDetailView, AddCommentView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("add-comment/<int:pk>", AddCommentView.as_view(), name="add-comment"),
]


app_name = "blog"
