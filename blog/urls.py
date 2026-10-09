from django.urls import path
from .views import post_detail, Index

app_name = "blog"

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("posts/<int:pk>/", post_detail, name="post-detail"),
]
