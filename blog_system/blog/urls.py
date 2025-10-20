from django.urls import path
from django.views.generic import DetailView

from .views import IndexView, PostDetailView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),
]
