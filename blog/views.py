from typing import Any

from django.http import (
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
    HttpResponse
)
from django.shortcuts import redirect
from django.views import generic

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    template_name = "blog/post_detail.html"
    model = Post

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = context["post"]
        comments = Commentary.objects.filter(post=post).select_related("user")

        context["comments"] = comments
        context["form"] = CommentaryForm()
        return context

    def post(
            self, request, *args, **kwargs
    ) -> HttpResponsePermanentRedirect | HttpResponseRedirect | HttpResponse:
        post = self.get_object()
        form = CommentaryForm(request.POST or None)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect("blog:post-detail", pk=post.pk)

        return self.render_to_response(self.get_context_data(form=form))
