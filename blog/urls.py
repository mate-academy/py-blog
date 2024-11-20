from django.urls import path
from .views import PostDetailView, CustomLoginView, PostListView

urlpatterns = [
    path("", PostListView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
]

app_name = "blog"
