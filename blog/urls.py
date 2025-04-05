from django.urls import path
from blog.views import IndexView, PostDetailView, SignUpView

app_name = "blog"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
