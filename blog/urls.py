from django.urls import path

import blog
from blog.views import index, PostDetailView

urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]