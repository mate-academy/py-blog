from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
]
