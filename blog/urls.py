from django.urls import path

from blog.views import (
    IndexListView,
    PostDetailView,
    PostCreateView,
    PostDeleteView,
    PostUpdateView,
    edit_comment,
    delete_comment,
)

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/delete/",
         PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/update/",
         PostUpdateView.as_view(), name="post-update"),
    path("comment/<int:pk>/edit/", edit_comment, name="edit-comment"),
    path("comment/<int:pk>/delete/", delete_comment, name="delete-comment"),
]

app_name = "blog"
