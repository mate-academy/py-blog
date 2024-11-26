from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import index, PostDetailView, RegisterView

app_name = "blog"

urlpatterns = [
    path(
        "", index, name="index"),
    path(
        "post/<int:pk>/", PostDetailView.as_view(), name="post-detail"
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(),
        name="login"
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),
    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),
]
