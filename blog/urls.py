from django.contrib import admin
from django.urls import path

from blog.views import PostListView, post_detail


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", post_detail, name="post-detail"),
]


app_name = "blog"
