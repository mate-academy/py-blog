from django.urls import reverse
from django.views import generic

from .forms import CommentForm
from .models import Post, Commentary


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    ordering = ["-created_time"]
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_success_url(self):
        return reverse(
            "blog:post-detail",
            kwargs={"pk": self.object.pk}
        )


class CommentCreateView(generic.CreateView):
    model = Commentary
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs["pk"]
        self.success_url = reverse(
            "blog:post-detail",
            kwargs={"pk": form.instance.post_id}
        )
        return super().form_valid(form)
