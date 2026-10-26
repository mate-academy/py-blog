from blog.views import IndexView, PostDetailView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),

]

app_name = "blog"
