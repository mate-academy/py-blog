from django.urls import path
from .views import (
    index,
    post_detail,
)


app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", post_detail, name="post-detail")
    ]
