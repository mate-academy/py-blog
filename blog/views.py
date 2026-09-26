from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import DetailView

from .models import Post

from .forms import CommentaryForm


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.order_by("-created_time")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "index.html", context={"post_list": page_obj})


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in context:
            context["form"] = CommentaryForm()
        return context

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.object = self.get_object()

        form = CommentaryForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(
                "content",
                "You must be logged in to add a comment."
            )
            context = self.get_context_data(form=form)
            return self.render_to_response(context)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = self.get_object()
            comment.save()

            return redirect(
                "blog:post-detail",
                pk=self.get_object().pk
            )

        context = self.get_context_data(form=form)
        return self.render_to_response(context)
