from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary, User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserCreateView(generic.CreateView):
    model = User
    form_class = RegisterForm
    template_name = "registration/sign-up.html"
    success_url = reverse_lazy("blog:index")


class PostListView(generic.ListView):
    model = Post
    ordering = ["-created_time"]
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetatilView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    template_name = "blog/create-comment.html"
    fields = ("content", )

    def post(self, request, *args, **kwargs):
        user = request.user
        pk = kwargs.get("pk")
        post = get_object_or_404(Post, pk=pk)
        text = request.POST["content"]
        if text:
            Commentary.objects.create(user=user, post=post, content=text)
            return redirect("blog:post-detail", pk=pk)
