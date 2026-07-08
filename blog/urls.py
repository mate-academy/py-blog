from django.urls import path

from blog import views


urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:pk>/", views.post_detail, name="post-detail"),
]

app_name = "blog"
