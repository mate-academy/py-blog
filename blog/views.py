from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.forms import CustomUserCreationForm
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related("commentary_set")
    template_name = "blog/index.html"


class PostDetailView(generic.DetailView):
    model = Post

    def get_queryset(self):
        return Post.objects.select_related("owner").prefetch_related("commentary_set__user")


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    model = get_user_model()
    template_name = "registration/sign_up.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse("blog:index")
