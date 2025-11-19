from django.urls import path

from blog.views import index, PostDetailView
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"