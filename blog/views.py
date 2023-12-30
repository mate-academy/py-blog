from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryCreateForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all().select_related("owner")
    page_number = request.GET.get(key="page")
    paginator = Paginator(post_list, 5)
    post_list = paginator.get_page(page_number)
    page_obj = paginator.get_page(page_number)
    num_pages = paginator.num_pages
    context = {
        "post_list": post_list,
        "page_obj": page_obj,
        "num_pages": num_pages
    }
    return render(request, "blog/index.html", context)


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryCreateForm()
        return context

    def post(self, request, **kwargs):
        content = request.POST["content"]
        user = request.user
        post_id = kwargs["pk"]
        comment = Commentary(content=content, user=user, post_id=post_id)
        comment.save()
        return HttpResponseRedirect(
            reverse_lazy("blog:post-detail", args=[post_id])
        )
