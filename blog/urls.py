from django.urls import path

from blog.views import index, post_detail


urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", post_detail, name="post-detail"),
]

app_name = "blog"
