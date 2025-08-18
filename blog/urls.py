from django.contrib import admin
from django.urls import path
from django.views.generic import detail

from blog.views import IndexView, PostDetailView

app_name = "blog"


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
