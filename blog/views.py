from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.core.paginator import Paginator

from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "post_list": page_obj,
        "page_obj": page_obj,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.commentary_set.all()
        return context
