from django.urls import path
from . import views
from .views import PostDetailView


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]

app_name = 'blog'
