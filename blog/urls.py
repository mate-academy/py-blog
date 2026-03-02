
from django.urls import include, path
from blog.views import PostDetailView, IndexListView

app_name = 'blog'

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

]

