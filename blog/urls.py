from django.urls import path

from blog import views
from blog.views import (index,
                        PostDetailView)


urlpatterns = [
    path("", index, name="index"),
    path("posts/pk/", PostDetailView.as_view(), name="post-detail"),
]


app_name = "blog"
