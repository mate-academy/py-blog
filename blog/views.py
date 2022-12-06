from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentaryForm, AuthUserForm, RegisterUserForm
from blog.models import Post, User


def index(request):
    """View function for the home page of the site."""

    post_list = Post.objects.all().order_by("-created_time")
    paginator = Paginator(post_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": post_list,
        "page_obj": page_obj,
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post_list"
    form_class = CommentaryForm

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.get_object().id}
        )

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class BlogLoginView(LoginView):
    form_class = AuthUserForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("blog:index")

    def get_success_url(self):
        return self.success_url


class BlogLogoutView(LogoutView):
    next_page = reverse_lazy("blog:index")


class RegisterUserView(generic.CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("blog:index")
