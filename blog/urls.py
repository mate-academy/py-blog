from django.urls import path

from blog.views import index, post_detail


app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/", post_detail, name="post-detail"),
]
