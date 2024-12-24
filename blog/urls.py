from django.urls import path

from blog import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
]

app_name = "blog"