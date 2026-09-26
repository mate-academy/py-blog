from django.urls import path

from .views import index, PostDetailView

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", index, name="index"),
    path(
        "posts/<pk>/",
        PostDetailView.as_view(),
        name="post-detail"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

app_name = "blog"
