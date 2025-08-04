from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/create/", views.create_post, name="create_post"),
    path("posts/<int:pk>/", views.post_detail, name="post-detail"),
]
