from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.models import Post, Commentary, User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "registration/sign-up.html", {"form": form})

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "You have singed up successfully.")
            login(request, user)
            return HttpResponseRedirect(reverse("blog:index"))
        return render(request, "registration/sign-up.html", {"form": form})


class PostListView(generic.ListView):
    model = Post
    ordering = ["-created_time"]
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetatilView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"


@login_required
def create_comment(request: HttpRequest, pk: int) -> HttpResponse:
    context = {"comments": Post.objects.get(pk=pk).comments.all()}
    if request.method == "POST":
        user = request.user
        post = Post.objects.get(pk=pk)
        text = request.POST["content"]
        if text:
            Commentary.objects.create(user=user, post=post, content=text)
            return HttpResponseRedirect(f"/posts/{pk}/")
    return render(request, "blog/create-comment.html", context=context)


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    template_name = "blog/create-comment.html"
    fields = "__all__"
