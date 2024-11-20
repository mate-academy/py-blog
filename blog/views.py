from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.models import Post
from blog.forms import CommentForm


def index(request: HttpRequest) -> HttpResponse:
    posts = (
        Post.objects.select_related("owner")
        .prefetch_related("commentaries__user")
        .order_by("-created_time")
    )
    # print(post_list)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    post_list = paginator.get_page(page_number)
    return render(
        request,
        "blog/index.html",
        {
            "post_list": post_list,
        },
    )


class PostDetailView(FormMixin, generic.DetailView):
    template_name = "blog/post_detail.html"
    model = Post
    queryset = Post.objects.select_related("owner").prefetch_related(
        "commentaries__user"
    )
    form_class = CommentForm

    def get_success_url(self) -> str:
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )

    def post(self, request, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid() and request.user.is_authenticated:
            commentary = form.save(commit=False)
            commentary.user = request.user
            commentary.post = self.object
            commentary.save()
            return self.form_valid(form=form)
        return self.form_invalid(form=form)
