from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import FormMixin

from blog.forms import CommentForm
from blog.models import Post, Commentary


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    ordering = ["-created_time"]


class PostDetailView(FormMixin, generic.DetailView):
    model = Post
    form_class = CommentForm

    def __init__(self) -> None:
        super().__init__()
        self.object = None

    def get_success_url(self) -> reverse:
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs) -> render:
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            Commentary.objects.create(
                user_id=request.POST["user_id"],
                post_id=request.POST["post_id"],
                content=request.POST["content"],
            )
        return render(
            request,
            "blog/post_detail.html",
            context=self.get_context_data(**kwargs)
        )
