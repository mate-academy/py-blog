from django.urls import path
from .views import IndexView, PostDetailView, PostCreateView, CommentsCreateView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:post_id>/add_comm/', CommentsCreateView.as_view(), name='add-comment'),
]