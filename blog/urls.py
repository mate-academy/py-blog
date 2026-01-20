from django.urls import path

from blog.views import index, post_detail_view

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", post_detail_view, name="post-detail"),
]

app_name = "blog"
