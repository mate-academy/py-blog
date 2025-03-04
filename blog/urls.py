from django.urls import path

from .views import PostListView, PostDetailView, commentary_create

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<str:pk>", PostDetailView.as_view(), name="post-detail"),

    path("posts/<str:pk>/commentary_create/", commentary_create,
         name="commentary-create"),
]

app_name = "blog"
