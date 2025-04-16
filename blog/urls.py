from .views import (
    index,
    PostDetailView,
    PostCreateView,

)
from django.urls import path


urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/create/", PostCreateView.as_view(),
         name="post-create"),
    ]

app_name = "blog"
