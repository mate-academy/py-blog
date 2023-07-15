from django.urls import path

from blog.views import IndexView, post_detail_view

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/<int:pk>", post_detail_view, name="post-detail")
]

app_name = "blog"
