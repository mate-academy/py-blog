from django.urls import path
from .views import index, PostDetailView

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    # path("logout/", logout, name='logout'),
]
