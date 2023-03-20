from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from blog.models import Post, Commentary
from blog.forms import CommentCreateForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all().select_related("owner").prefetch_related("commentary")
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post

    def get_queryset(self):
        queryset = Post.objects.select_related("owner").prefetch_related("commentary")
        queryset.filter(id=self.kwargs.get(self.pk_url_kwarg))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentCreateForm

        return context

    def post(self, request, pk=None):
        form = CommentCreateForm(request.POST)
        url = reverse_lazy("blog:post-detail", kwargs={"pk": pk})
        if form.is_valid() and pk:
            Commentary.objects.create(
                user_id=self.request.user.pk,
                post_id=pk,
                content=form.cleaned_data["content"]
            )
        return HttpResponseRedirect(url)
