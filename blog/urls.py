from django.contrib.auth import views as auth_views
from django.urls import path

from blog import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path("posts/<int:pk>/",
         views.PostDetailView.as_view(),
         name="post-detail"),
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
