from django.urls import path

from .views import (index, PostListView, PostDetailView)

urlpatterns = [
    path("", PostListView.as_view(), name="index"),

    path("posts/", PostListView.as_view(), name="post-list"),

    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    # path("posts/create/", PostCreateView.as_view(), name="post-create"),
    # path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    # path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

    # path("commentaries/", CommentaryListView.as_view(), name="commentary-list"),
    # path("commentaries/<int:pk>/", CommentaryDetailView.as_view(), name="commentary-detail"),
    # path("commentaries/create/", CommentaryCreateView.as_view(), name="commentary-create"),
    # path("commentaries/<int:pk>/update/", CommentaryUpdateView.as_view(), name="commentary-update"),
    # path("commentaries/<int:pk>/delete/", CommentaryDeleteView.as_view(), name="commentary-delete"),

]

app_name = "blog"
