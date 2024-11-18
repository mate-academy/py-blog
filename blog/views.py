from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentaryForm

from .models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = (
        Post.objects.all()
        .prefetch_related("commentarys")
        .order_by("-created_time")
    )
    for post in posts:
        post.content = post.content[:80] + "..."
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": page_obj.object_list,
        "post_list": page_obj,
        "paginator": paginator,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.all().prefetch_related("commentarys")
    template_name = "blog/post_detail.html"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:post-list")
    template_name = "blog/post_form.html"


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["content"]
    template_name = "blog/commentary_form.html"

    def post(self, request, *args, **kwargs):
        print(request.POST)
        post = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = post
            commentary.user = self.request.user
            commentary.save()
        return redirect("blog:post-detail", pk=kwargs["pk"])

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail", 
            kwargs={"pk": self.object.post.pk}
        )
