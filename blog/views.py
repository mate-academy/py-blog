from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import DetailView
from blog.forms import CommentForm
from django.shortcuts import redirect

from blog.models import Post


def index(request):
    posts = (
        Post.objects
        .select_related("author")
        .prefetch_related("author__comments")
    )

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "post_list": page_obj.object_list,
        "page_obj": page_obj,
    }

    return render(request, "blog/main_page.html", context)


class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related("author")
            .prefetch_related("comments__author")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if not request.user.is_authenticated:
            form.add_error(None, "You must be logged in to comment")
            return self.render_to_response(
                self.get_context_data(form=form)
            )

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect("blog:post-detail", pk=self.object.pk)

        return self.render_to_response(
            self.get_context_data(form=form)
        )
