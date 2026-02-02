from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from blog.forms import CommentaryForm
from blog.models import Post, Commentary
from django.views import generic


# Create your views here.
# def index(request: HttpRequest) -> HttpResponse:
#     posts_queryset = Post.objects.all().order_by("-created_time")
#     paginator = Paginator(posts_queryset, 5)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     context = {
#         "page_obj": page_obj,
#         "posts": page_obj.object_list,
#         "is_paginated": page_obj.paginator.num_pages > 1,
#     }
#     return render(request, "blog/index.html", context=context)

def index(request: HttpRequest) -> HttpResponse:
    posts_queryset = Post.objects.all()
    paginator = Paginator(posts_queryset, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "post_list": page_obj.object_list,
        "is_paginated": page_obj.paginator.num_pages > 1,
    }
    return render(request, "blog/index.html", context=context)


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

    class Meta:
        ordering = ["-created_time"]


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = CommentaryForm()
        return ctx


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    form_class = CommentaryForm

    def get(self, request, *args, **kwargs):
        return redirect("blog:post-detail", pk=kwargs["pk"])

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )


@login_required
def my_posts_view(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/my_posts.html")
