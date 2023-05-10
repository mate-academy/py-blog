from django.urls import path

from blog.views import (PostListView,
                        PostDetailView,
                        PostAddView,
                        PostUpdateView,
                        PostDeleteView)
from . import views


urlpatterns = [
    path("",
         PostListView.as_view(),
         name="index"),

    path("blog/<int:pk>",
         PostDetailView.as_view(),
         name="post-detail"),

    path("post_add/",
         PostAddView.as_view(),
         name="post-add"),

    path("blog/update/<int:pk>",
         PostUpdateView.as_view(),
         name="post-update"),

    path("blog/<int:pk>/delete/",
         PostDeleteView.as_view(),
         name="post-delete"),
]

app_name = "blog"
