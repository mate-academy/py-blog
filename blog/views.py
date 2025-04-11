from django.core.paginator import Paginator

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


def index(request: HttpRequest) -> HttpResponse:
    post_list = Post.objects.all().order_by("-created_time")

    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj.object_list,
        "page_obj": page_obj,
    }
    return render(request, "blog/index.html", context=context)


class PostDetailView(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context

    def post(self, request, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        form = CommentaryForm(request.POST)
        if form.is_valid():
            Commentary.objects.create(
                post=self.get_object(),
                user=request.user,
                content=request.POST.get("content"),
            )

            return HttpResponseRedirect(
                reverse(
                    "blog:post-detail",
                    kwargs={"pk": self.object.pk}
                )
            )
