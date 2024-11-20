"""blog_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from blog.views import (
    IndexView,
    PostDetailView,
    create_comment,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path(
        "posts/create-comment/<int:pk>", create_comment, name="create-comment"
    ),
    path("posts/create", PostCreateView.as_view(), name="post-create"),
    path(
        "posts/<int:pk>/update", PostUpdateView.as_view(), name="post-update"
    ),
    path(
        "posts/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"
    ),
]

app_name = "blog"
