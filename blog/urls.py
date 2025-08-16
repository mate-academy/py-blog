from django.urls import path

from blog.views import IndexView, PostDetailView

app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
