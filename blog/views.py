from django.urls import reverse_lazy
from django.views import generic

from blog.forms import CommentaryCreationForm
from blog.models import Commentary, Post


class PostListView(generic.ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    ordering = "-created_time"
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.commentary_set.all()
        context["comments"] = comments
        return context


class CommentaryCreateView(generic.CreateView):
    model = Commentary
    form_class = CommentaryCreationForm
    template_name = "blog/post_detail.html"

    def form_valid(self, form):
        post_id = self.kwargs["post_id"]
        post = Post.objects.get(pk=post_id)
        comment_content = form.cleaned_data["content"]
        comment_user = self.request.user
        comment = Commentary.objects.create(
            post=post, user=comment_user, content=comment_content
        )
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.object.post.pk}
        )
