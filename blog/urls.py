from django.urls import path
from .views import IndexView, PostDetailView, UserRegisterView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="blog:index"), name="logout"),
    path("register/", UserRegisterView.as_view(), name="register"),
]
