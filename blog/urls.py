from django.contrib import admin
from django.urls import path, include

from blog.views import IndexView, PostDetailView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail")
]

app_name = "blog"
