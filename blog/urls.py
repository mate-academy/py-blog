from django.urls import path

from blog.views import PostListView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
]