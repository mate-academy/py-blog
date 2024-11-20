from django.urls import path

from .views import index, post_detail_view, user_detail_view


urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", post_detail_view, name="post-detail"),
    path("users/<int:pk>/", user_detail_view, name="user-detail"),
]

app_name = "blog"
