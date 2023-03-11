from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Post
from .forms import CommentaryForm


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentaries")


class PostDetailView(generic.DetailView):
    model = Post
    queryset = Post.objects.select_related(
        "owner").prefetch_related("commentaries__user")

    def get_context_data(self, **kwargs: Any) -> Any:
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = CommentaryForm()
        return context


class CommentaryCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = CommentaryForm
    template_name = "blog/post_detail.html"

    def post(self, request: Any, *args: Any, **kwargs: Any) -> Any:
        post_id = kwargs["pk"]
        post_url = reverse("blog:post-detail", kwargs={"pk": post_id})
        form = CommentaryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            if content:
                form.instance.user_id = self.request.user.pk
                form.instance.post_id = post_id
                self.success_url = post_url
                return super().form_valid(form)

        return HttpResponseRedirect(post_url)
