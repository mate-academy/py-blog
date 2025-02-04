from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from blog.forms import CommentaryForm
from blog.models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 5
    queryset = Post.objects.select_related("owner")


class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentaryForm

    def get_success_url(self):
        return reverse_lazy("blog:post-detail", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = self.object
        form.save()
        return super().form_valid(form)


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]
    success_url = reverse_lazy("blog:post-list")
    template_name = "blog/post_form.html"