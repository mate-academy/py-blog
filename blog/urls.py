from django.urls import path

from blog.views import IndexView, postdetailview

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>", postdetailview, name="post-detail"),
]

app_name = "blog"
