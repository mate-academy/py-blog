from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from blog.forms import RegisterForm, CommentForm
from blog.models import Post, User


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    queryset = Post.objects.all().select_related("owner")
    template_name = "blog/home.html"
    paginate_by = 5

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super(PostListView, self).get_context_data(**kwargs)
        context["header_image_url"] = "assets/img/home.jpg"
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs) -> dict[str]:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


class RegisterView(generic.CreateView):
    model = User
    form_class = RegisterForm
    template_name = "blog/register.html"

    def form_valid(self, form: RegisterForm) -> HttpResponseRedirect:
        form.save()
        customer = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, customer)
        return HttpResponseRedirect(reverse("blog:index"))


def about(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "blog/about.html",
        context={
            "name": "about",
            "header_image_url": "assets/img/about.jpg",
        },
    )


def contact(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "blog/contact.html",
        context={
            "name": "contact",
            "header_image_url": "assets/img/contact.jpg",
        },
    )
