from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CommentForm
from .models import Post, Commentary


# Create your views here.
def index(request):
    post = Post.objects.order_by("-created_time")
    commentary = Commentary.objects.count()
    paginator = Paginator(post, 5)
    page_number = request.GET.get("page")
    post_list = paginator.get_page(page_number)

    context = {
        "post_list": post_list,
        "commentary": commentary,
    }

    return render(request, "blog/index.html", context)


class PostListView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class UserLoginView(LoginView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("blog:index")


class UserLogoutView(LogoutView):
    template_name = "registration/login.html"
    success_url = reverse_lazy("blog:index")


class PostAddComment(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = "blog/add_comment.html"
    context_object_name = "post_add"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm(request=self.request)
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
        return super().get(request, *args, **kwargs)
