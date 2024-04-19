from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from blog.forms import CommentaryForm
from blog.models import Post

from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "blog/index.html"
    queryset = (
        Post.objects.all().select_related
        ("owner").order_by("-created_time")
    )
    paginate_by = 5


class PostDetailView(DetailView, CreateView):
    model = Post
    template_name = "blog/post_detail.html"
    form_class = CommentaryForm

    def form_valid(self, form):
        form.instance.post = Post.objects.get(pk=self.kwargs["pk"])
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "blog:post-detail",
            kwargs={"pk": self.kwargs["pk"]}
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context
