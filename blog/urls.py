from .views import index
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "blog"
urlpatterns = [
    path("", index, name="index"),
    path("post/<int:pk>/", views.post_detail_view, name="post-detail"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
