from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic

from .forms import *
from .models import *

LOGIN_CURL = "login_curl"
LOGIN_ERROR = "login_error"
LOGIN_USERNAME = "login_username"


def login_view(request):
    if request.method == "GET":
        src_url = request.GET.get(LOGIN_CURL, "")
    else:
        src_url = request.POST.get(LOGIN_CURL, "")
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        request.session[LOGIN_ERROR] = ""
        request.session[LOGIN_USERNAME] = ""

        if user:
            login(request, user)
        elif username:
            request.session[LOGIN_ERROR] = "Invalid credentials"
            request.session[LOGIN_USERNAME] = username

    return HttpResponseRedirect(src_url)


def logout_view(request):
    src_url = request.POST.get(LOGIN_CURL, "")
    logout(request)

    return HttpResponseRedirect(src_url)


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    queryset = Post.objects.all().order_by("-created_time")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AddCommentForm()
        return context


class AddCommentView(LoginRequiredMixin, generic.CreateView):
    def post(self, request, *args, **kwargs):
        post_id = kwargs["pk"]
        post_url = reverse("blog:post-detail", kwargs={"pk": post_id})
        form = AddCommentForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data["content"]

            if post_id and content:
                form.instance.user_id = self.request.user.pk
                form.instance.post_id = post_id
                self.success_url = post_url
                return super().form_valid(form)

        return HttpResponseRedirect(post_url)
