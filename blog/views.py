from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import RegisterForm, CommentForm
from blog.models import Post, User


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs) -> HttpResponse:
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)
        return self.get(request, *args, **kwargs)


@login_required
def profile_view(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/profile.html")


class RegisterView(generic.FormView):
    model = User
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("blog:profile")

    def form_valid(self, form: RegisterForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)
