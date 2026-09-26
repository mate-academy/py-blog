from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.core.paginator import Paginator

from blog.forms import CommentaryForm
from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-created_time")
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)

    context = {
        "post_list": page,
    }

    return render(request, "blog/index.html", context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "form" not in kwargs:
            context["form"] = CommentaryForm()

        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        self.object = self.get_object()
        form = CommentaryForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(
                None, "Only authenticated users can leave a commentary"
            )

            return self.render_to_response(self.get_context_data(form=form))

        if form.is_valid():
            commentary = form.save(commit=False)
            commentary.post = self.object
            commentary.user = request.user
            commentary.save()

            return redirect("blog:post-detail", pk=self.object.pk)

        return self.render_to_response(self.get_context_data(form=form))
