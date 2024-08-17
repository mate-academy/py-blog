from django.urls import path
from . import views
from .views import PostDetailView, CommentaryCreateView

app_name = 'blog'

urlpatterns = [
    path('index/', views.PostListView.as_view(), name='index'),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path('post/<int:post_id>/comment/', CommentaryCreateView.as_view(), name='commentary-create'),

]
