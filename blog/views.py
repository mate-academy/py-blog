from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView

from blog.forms import CommentForm
from blog.models import Post, Commentary


class IndexView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "post_list"
    paginate_by = 5
    ordering = ["-created_time"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Commentary.objects.all()
        return context


class PostDetailWithCommentView(DetailView, FormView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post-detail"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("blog:post-detail", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        context["form"] = context.get("form", self.get_form())
        return context

def form_valid(self, form):
    if not self.request.user.is_authenticated:
        return self.form_invalid(form)
    comment = form.save(commit=False)
    comment.post = self.get_object()
    comment.user = self.request.user
    comment.save()
    return super().form_valid(form)
