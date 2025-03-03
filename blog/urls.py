from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from blog.views import index, PostDetailView

app_name = 'blog'

urlpatterns = [
    path("", index, name="index"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]