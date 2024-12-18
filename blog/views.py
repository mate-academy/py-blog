from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary, User


def index(request: HttpRequest) -> HttpResponse:
    num_posts = Post.objects.count()
    num_users = User.objects.count()

    context = {
        "posts": num_posts,
        "users": num_users,
    }

    return render(
        request,
        "blog/index.html",
        context=context,
    )


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    template_name = "blog/post_list.html"
    context_object_name = "post_list"


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ["content"]


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        context["comments"] = Commentary.objects.select_related("post")
        return context


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        comment = form.save(commit=False)
        comment.post = post
        comment.user = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "blog/user_list.html"
    context_object_name = "user_list"


class UserCreateView(generic.CreateView):
    model = User
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "password"
    ]
    success_url = reverse_lazy("blog:user-list")
    template_name = "blog/user_create.html"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["password"].widget = forms.PasswordInput()
        form.fields["username"].help_text = ""
        return form

    def form_valid(self, form):
        form.instance.password = make_password(form.cleaned_data["password"])
        return super().form_valid(form)
