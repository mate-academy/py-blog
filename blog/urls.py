from django.urls import path

from .views import (
    Index,
    PostDetailView,
    add_comment,
    PostCreateView,

)


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("add_comment/<int:pk>/", add_comment, name="add-comment"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
]

app_name = "taxi"
