from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin, ProcessFormView

from blog.forms import CommentaryForm
from blog.models import Post, Commentary


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, FormMixin, ProcessFormView, generic.DetailView):
    form_class = CommentaryForm
    model = Commentary
    template_name = "blog/post_detail.html"
    success_url = reverse_lazy("blog:index")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object = None

    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["post"] = Post.objects.get(pk=self.kwargs["pk"])
        context["user"] = self.request.user
        return context
