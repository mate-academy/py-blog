from django.urls import path, include

from blog.views import IndexView, PostDetailtView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("posts/<int:pk>/", PostDetailtView.as_view(), name="post-detail"),
]

app_name = "blog"
