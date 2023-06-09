from django.urls import path

from blog.views import PostListView, PostDetailView, AddCommentView

urlpatterns = [
    path("post", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    # path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    # path("post/<int:pk>/add-comment", post_detail, name="add-comment"),
    path("post/<int:pk>/comment/", AddCommentView.as_view(), name="add-comment")

]


app_name = "blog"
