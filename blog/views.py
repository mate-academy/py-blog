from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    ordering = "-created_time"
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentaries")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentaries", "commentaries__user")

    def get_context_data(self, **kwargs: Any) -> dict[str: Any]:
        context = super().get_context_data(**kwargs)
        context.update(form=CommentaryForm())
        return context

    def post(
            self,
            request: HttpRequest,
            *args: Any,
            **kwargs: Any
    ) -> HttpResponse:
        post = get_object_or_404(Post, pk=kwargs["pk"])
        form = CommentaryForm(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            Commentary.objects.create(
                user=request.user,
                post=post,
                content=form.cleaned_data["content"]
            )
            return super().get(request, args, kwargs)

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context["form"] = form
        return self.render_to_response(context)
