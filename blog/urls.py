from django.urls import path

from blog.views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    # path("post/<int:pk>/comment/", add_comment, name="add-comment")

]


app_name = "blog"
