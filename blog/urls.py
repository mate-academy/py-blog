from django.urls import path

from blog.views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path(""
         "post/detail/<int:pk>/",
         PostDetailView.as_view(),
         name="post-details"
         ),
    path(""
         "post/create/<int:pk>/",
         PostCreateView.as_view(),
         name="post-create"
         ),
]

app_name = "blog"
