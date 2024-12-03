from django.urls import path

from blog.views import IndexListView, post_detail_view

urlpatterns = [
   path("", IndexListView.as_view(), name="index-list"),
   path("posts/<int:pk>", post_detail_view, name="post-detail"),
]

app_name = "blog"
