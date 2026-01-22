from django.urls import path

from blog.views import index

from blog.views import PostDetailView

urlpatterns = [
    path("index/", index, name="index"),
    path("index/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
