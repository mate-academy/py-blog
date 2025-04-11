from django.urls import path

from blog.views import index, PostDetailView

urlpatterns = [
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("index/", index, name="index"),
]

app_name = "blog"
