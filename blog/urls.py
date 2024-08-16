from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('index/', views.PostListView.as_view(), name='index'),
]
