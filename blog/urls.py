from operator import index

from django.urls import path
from . import views
from .views import PostDetailView


urlpatterns = [
    path("", index, name="index"),
    path("", views.home, name="index"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]

app_name = "blog"
