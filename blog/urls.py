from django.urls import path

from blog.views import (
    index,
    PostDetailView,
    BlogLoginView,
    RegisterUserView,
    BlogLogoutView)

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("login/", BlogLoginView.as_view(), name="login-page"),
    path("register/", RegisterUserView.as_view(), name="register-page"),
    path("logout/", BlogLogoutView.as_view(), name="logout-page")
]

app_name = "blog"
