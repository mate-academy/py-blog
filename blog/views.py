from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from .models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts, 5)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    context = {
        "page_obj": page_obj,
        "post_list": page_obj.object_list,
    }
    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView):
    model = Post


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Commentary
    fields = ["post", "user", "content"]
    template_name = "blog/commentary_form.html"

    def get_success_url(self):
        post_pk = self.object.post.pk
        return reverse("blog:post-detail", kwargs={"pk": post_pk})
