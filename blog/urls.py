from django.urls import path
from blog.views import index, PostDetailView

urlpatterns = [
    path("posts/", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"
